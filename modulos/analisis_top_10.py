def calcular_top10_manufactura(df_manufactura):
    """
    Calcula los roles de Manufactura con mayor puntaje
    promedio de reemplazo por IA.
    """

    top10 = (
        df_manufactura
        .groupby("rol_laboral")["puntaje_reemplazo_ia"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )

    return top10

def interpretar_top10_manufactura(top10):

    conclusion = """
    Los roles operativos y de atención (Conductor de Camión, Representante de
    Atención al Cliente) presentan el mayor riesgo de reemplazo. Los roles
    técnicos especializados (Ingeniero de Software, Analista de Datos)
    muestran el menor riesgo relativo. Esto sugiere que, dentro de una misma
    industria, el riesgo de automatización depende más de la naturaleza de la
    tarea que del sector en sí.
    """

    return conclusion