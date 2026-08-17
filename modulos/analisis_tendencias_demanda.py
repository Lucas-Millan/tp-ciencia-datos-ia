def calcular_tendencia_demanda(df):
    """
    Calcula el crecimiento promedio anual de demanda de habilidades.
    """

    tendencia = (
        df.groupby("año")["porcentaje_crecimiento_demanda_habilidades"]
        .mean()
        .reset_index()
    )

    tendencia["variacion"] = (
        tendencia["porcentaje_crecimiento_demanda_habilidades"]
        .diff()
    )

    return tendencia

def analizar_tendencias_demanda(df_limpio, df_manufactura):

    tendencia_global = calcular_tendencia_demanda(df_limpio)

    tendencia_manufactura = calcular_tendencia_demanda(df_manufactura)


    print("\nTendencia global:")
    print(tendencia_global.round(4))


    print("\nTendencia Manufactura:")
    print(tendencia_manufactura.round(4))


    conclusion_global = """¿Se está acelerando la necesidad de perfiles híbridos (Dataset completo)? No.
    El valor final es apenas superior al valor inicial tras seis años de fluctuación.
    El comportamiento observado es de fluctuación cíclica alrededor de un promedio
    estable, sin tendencia de crecimiento sostenido."""

    conclusion_manufactura = """¿Se está acelerando en Manufactura? No, y el resultado es más desfavorable
    que a nivel general: el valor final queda por debajo del valor inicial, con
    una volatilidad año a año claramente mayor que el resto de la economía
    representada en el dataset."""

    conclusion_general = """Conclusión general: ni a nivel general ni en Manufactura hay evidencia de
    aceleración sostenida en la necesidad de perfiles híbridos. Manufactura,
    además, muestra una dinámica más inestable y, en términos netos del
    período, regresiva."""

    print(conclusion_global)
    print(conclusion_manufactura)
    print(conclusion_general)


    return {
        "global": tendencia_global,
        "manufactura": tendencia_manufactura,
        "conclusion_global": conclusion_global,
        "conclusion_manufactura": conclusion_manufactura,
        "conclusion_general": conclusion_general
    }