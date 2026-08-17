import numpy as np
import pandas as pd

def eliminar_duplicados(df_limpio):
    # --- Duplicados ---
    # La coincidencia exacta en job_id confirma que son errores de ingesta,
    # no observaciones independientes.
    df_limpio.drop_duplicates(inplace=True)

def normalizacion_industry(df_limpio):
    # --- Normalización de 'industry' ---
    # strip() quita espacios; title() unifica el case (FINANCE / finance -> Finance).
    df_limpio['industry'] = df_limpio['industry'].str.strip().str.title()

def correccion_tipos(df_limpio):
    # --- Corrección de tipos ---
    df_limpio['year'] = pd.to_numeric(df_limpio['year'], errors='coerce').astype('Int64')
    df_limpio['salary_before_usd'] = (
        df_limpio['salary_before_usd'].str.replace(r'[\$,]', '', regex=True).astype(float)
    )
    df_limpio['salary_after_usd'] = (
        df_limpio['salary_after_usd'].str.replace(r'[\$,]', '', regex=True).astype(float)
    )

def eliminar_centinela(df_limpio):
    # --- Valor centinela ---
    # -99999 es un código manual de "dato faltante", no una variación aleatoria.
    # Se convierte a NaN para no distorsionar media, mínimo y correlaciones.
    df_limpio['salary_before_usd'] = df_limpio['salary_before_usd'].replace(-99999, np.nan)

def valores_fuera_de_escala(df_limpio):
# --- Valores fuera de escala ---
    # ai_replacement_score tiene escala declarada 0-100; se acotan los valores
    # que la superan (hasta 113.07 detectado en la auditoría).
    df_limpio['ai_replacement_score'] = df_limpio['ai_replacement_score'].clip(upper=100)

def imputacion_datos(df_limpio):
    # --- Imputación de nulos ---
    # Salarios y riesgo de automatización: mediana agrupada por rol laboral.
    # La mediana es robusta a outliers; agrupar por rol respeta que distintos
    # puestos tienen distribuciones salariales y de riesgo muy distintas.
    medianas_salario_antes = df_limpio.groupby('job_role')['salary_before_usd'].transform('median')
    df_limpio['salary_before_usd'] = df_limpio['salary_before_usd'].fillna(medianas_salario_antes)

    medianas_salario_despues = df_limpio.groupby('job_role')['salary_after_usd'].transform('median')
    df_limpio['salary_after_usd'] = df_limpio['salary_after_usd'].fillna(medianas_salario_despues)

    medianas_riesgo = df_limpio.groupby('job_role')['automation_risk_percent'].transform('median')
    df_limpio['automation_risk_percent'] = df_limpio['automation_risk_percent'].fillna(medianas_riesgo)

    # Industria: moda global (no hay variable auxiliar confiable para inferirla).
    moda_industria = df_limpio['industry'].mode()[0]
    df_limpio['industry'] = df_limpio['industry'].fillna(moda_industria)


def limpiar_dataset(df):
    """
    Aplica el protocolo de curación completo sobre una copia del dataset
    original. Cada paso está comentado con su justificación técnica.

    Devuelve un nuevo DataFrame limpio (no modifica el original).
    """
    df_limpio = df.copy()

    eliminar_duplicados(df_limpio)
    normalizacion_industry(df_limpio)
    correccion_tipos(df_limpio)
    eliminar_centinela(df_limpio)
    valores_fuera_de_escala(df_limpio)
    imputacion_datos(df_limpio)

    return df_limpio
