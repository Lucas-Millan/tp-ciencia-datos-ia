import numpy as np


def calcular_bins_freedman_diaconis(df, columna):
    """
    Calcula la cantidad óptima de bins usando
    la regla de Freedman-Diaconis.
    """

    datos = df[columna]

    q1, q3 = np.percentile(datos, [25, 75])

    iqr = q3 - q1

    n = len(datos)

    ancho_bin = (2 * iqr) / (n ** (1 / 3))

    rango = datos.max() - datos.min()

    cantidad_bins = int(np.ceil(rango / ancho_bin))

    return cantidad_bins

def analizar_distribucion_salarios(df_limpio):
    """
    Obtiene métricas necesarias para analizar
    la distribución salarial.
    """

    bins = calcular_bins_freedman_diaconis(
        df_limpio,
        "salario_despues_usd"
    )

    resultado = {
        "media": df_limpio["salario_despues_usd"].mean(),
        "mediana": df_limpio["salario_despues_usd"].median(),
        "bins": bins
    }

    return resultado

def interpretar_distribucion_salarios():
    
    return """
    Las ocho industrias presentan distribuciones aproximadamente normales,
    centradas entre 75.000 y 100.000 USD. El hallazgo más notable es el pico
    pronunciado de Manufactura en el rango de 85.000-90.000 USD, con densidad
    claramente superior al resto. Se recortó el eje X a 200.000 USD dado que
    el dataset contiene valores atípicos extremos (máximo ~1.094.000 USD).
    """