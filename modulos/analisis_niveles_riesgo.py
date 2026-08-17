def calcular_riesgo_manufactura(df_manufactura):
    """
    Calcula la distribución porcentual de riesgo
    dentro de Manufactura.
    """

    conteo_riesgo = (
        df_manufactura["categoria_riesgo_automatizacion"]
        .value_counts(normalize=True)
        * 100
    )

    return conteo_riesgo


def calcular_riesgo_por_industria(df_limpio):
    """
    Calcula el porcentaje de trabajadores en Alto Riesgo
    para cada industria.
    """

    riesgo_por_industria = (
        df_limpio
        .groupby("industria")["categoria_riesgo_automatizacion"]
        .apply(lambda x: (x == "Alto").mean() * 100)
        .sort_values(ascending=False)
    )

    return riesgo_por_industria


def analizar_niveles_riesgo(df_limpio, df_manufactura):
    """
    Analiza el nivel de riesgo de automatización
    en Manufactura y lo compara con otras industrias.
    """

    riesgo_manufactura = calcular_riesgo_manufactura(df_manufactura)

    riesgo_industrias = calcular_riesgo_por_industria(df_limpio)


    porcentaje_alto_riesgo = (riesgo_manufactura.get("Alto", 0))


    print(
        f"\nPorcentaje de trabajadores de Manufactura "
        f"en 'Alto Riesgo': {porcentaje_alto_riesgo:.2f}%"
    )

    print("\nDistribución del riesgo en Manufactura:")
    print(
        riesgo_manufactura.apply(
            lambda x: f"{x:.2f}%"
        )
    )


    print("\nPorcentaje de Alto Riesgo por industria:")
    print(riesgo_industrias.round(2))


    conclusion = """
    Análisis: el 30.90% de los trabajadores de Manufactura está en categoría de
    Alto Riesgo. Sin embargo, al comparar con el resto de las industrias, este
    valor no se distingue significativamente: todas oscilan en una banda
    relativamente estrecha (28%-33%). Esto sugiere que el riesgo de
    automatización está distribuido de forma homogénea entre sectores, sin
    concentración marcada en industrias asociadas a trabajo manual.
    """

    print(conclusion)


    return {
        "riesgo_manufactura": riesgo_manufactura,
        "riesgo_por_industria": riesgo_industrias,
        "conclusion": conclusion
    }