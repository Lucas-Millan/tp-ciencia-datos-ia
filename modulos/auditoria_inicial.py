def dimensiones_iniciales(df):
    print(f"\nDimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")

def tipos_de_datos_iniciales(df):     
    print("\n--- Tipos de datos ---")
    print(df.info())
    print("""
    Anomalías de tipo detectadas:
    - 'year' es float, no entero.
    - 'salary_before_usd' y 'salary_after_usd' son objetos (texto), no float.
    """)

def nulos_iniciales(df):
    print("\n--- Valores nulos ---")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0])

def duplicados_iniciales(df):
    print("\n--- Duplicados ---")
    print(f"Filas completamente duplicadas: {df.duplicated().sum()}")
    print(f"job_id duplicados: {df['job_id'].duplicated().sum()}")

def estadisticos_descriptivos_iniciales(df):
    print("\n--- Estadísticos descriptivos ---")
    print(df.describe())
    print("""
    Anomalías de rango detectadas:
    - El mínimo de 'salary_before_usd' es -99999 (valor centinela).
    - El máximo de 'ai_replacement_score' es 113.07 (fuera de la escala 0-100).
    """)

def formato_cols_categoricas_iniciales(df):
    print("\n--- Inconsistencias de formato en columnas categóricas ---")
    print(f"'industry' tiene {df['industry'].nunique()} valores únicos (deberían ser 8):")
    print(df['industry'].value_counts())
    print("""
    Pandas distingue mayúsculas de minúsculas: una misma industria escrita de formas
    distintas (Finance, finance, FINANCE) se contabiliza como categorías separadas.
    """)

def auditar_calidad(df):
    """
    Reporte inicial sobre el estado de la información: identifica
    inconsistencias lógicas, errores de formato y vacíos de datos.

    No modifica el DataFrame, solo lo inspecciona e imprime hallazgos.
    """

    dimensiones_iniciales(df)
    tipos_de_datos_iniciales(df)
    nulos_iniciales(df)
    duplicados_iniciales(df)
    estadisticos_descriptivos_iniciales(df)
    formato_cols_categoricas_iniciales(df) 