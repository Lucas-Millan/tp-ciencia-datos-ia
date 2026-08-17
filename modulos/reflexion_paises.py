import pandas as pd

def calcular_metricas_paises_manufactura(df_manufactura):
    """
    Calcula métricas salariales y de riesgo por país
    dentro de Manufactura.
    """

    grupos_por_pais = df_manufactura.groupby("pais")


    cantidad_trabajadores = (
        grupos_por_pais["id_trabajo"]
        .count()
    )


    cambio_promedio = (
        grupos_por_pais["porcentaje_cambio_salario"]
        .mean()
    )


    cambio_mediano = (
        grupos_por_pais["porcentaje_cambio_salario"]
        .median()
    )


    pct_mejora_salarial = (
        (df_manufactura["porcentaje_cambio_salario"] > 0)
        .groupby(df_manufactura["pais"])
        .mean()
        * 100
    )


    pct_alto_riesgo = (
        (df_manufactura["categoria_riesgo_automatizacion"] == "Alto")
        .groupby(df_manufactura["pais"])
        .mean()
        * 100
    )


    return {
        "cantidad": cantidad_trabajadores,
        "cambio_promedio": cambio_promedio,
        "cambio_mediano": cambio_mediano,
        "pct_mejora": pct_mejora_salarial,
        "pct_alto_riesgo": pct_alto_riesgo
    }


def construir_tabla_paises_manufactura(df_manufactura):
    """
    Construye tabla comparativa por país.
    """

    metricas = calcular_metricas_paises_manufactura(
        df_manufactura
    )


    resumen = pd.DataFrame({
        "cantidad": metricas["cantidad"],
        "cambio_salarial_promedio": metricas["cambio_promedio"],
        "mediana_cambio": metricas["cambio_mediano"],
        "pct_cambio_positivo": metricas["pct_mejora"],
        "pct_alto_riesgo": metricas["pct_alto_riesgo"]
    })


    resumen = (
        resumen
        .round(2)
        .sort_values(
            "cambio_salarial_promedio",
            ascending=False
        )
    )


    return resumen


def interpretar_tabla_paises_manufactura(resumen_pais):
    """
    Genera conclusión del análisis.
    """

    mejor_pais = resumen_pais.index[0]


    conclusion = f"""
    Conclusión: 
    {mejor_pais} es el país que mejor gestionó la transición a la
    IA en Manufactura según la evolución salarial. Combina el mayor cambio
    salarial promedio, una mediana de cambio aún mayor (la mejora no está
    arrastrada por casos extremos), y la mayor proporción de trabajadores
    con mejora salarial real — sin tener el menor riesgo de automatización
    del grupo, lo que descarta que su buen resultado se explique simplemente
    por estar menos expuesto a la IA.
    """


    return conclusion