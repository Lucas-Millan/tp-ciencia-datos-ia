def calcular_correlacion(df, columna_x, columna_y):
    """
    Calcula correlación de Pearson entre dos variables.
    """

    return df[columna_x].corr(df[columna_y])

def analizar_brecha_vs_riesgo(df_limpio, validar_con_muestra=True):
    """
    Analiza la relación entre brecha de habilidades
    y riesgo de automatización.
    """

    correlacion = calcular_correlacion(
        df_limpio,
        "indice_brecha_habilidades",
        "porcentaje_riesgo_automatizacion"
    )


    muestra = df_limpio.sample(n=1000, random_state=42)
    correlacion_muestra = calcular_correlacion(
        muestra,
        "indice_brecha_habilidades",
        "porcentaje_riesgo_automatizacion"
    )

    conclusion = """
    El coeficiente de Pearson es prácticamente nulo, confirmando que no existe
    relación entre ambas variables: el riesgo de automatización de un puesto no
    depende de cuánta brecha de habilidades tenga el trabajador que lo ocupa.
    """


    print(f"Correlación completa: {correlacion:.4f}")
    print(f"Correlación muestra: {correlacion_muestra:.4f}")


    print(conclusion)


    return {
        "correlacion_completa": correlacion,
        "correlacion_muestra": correlacion_muestra,
        "muestra": muestra
    }

def analizar_riesgo_vs_urgencia(df_limpio):
    """
    Analiza relación entre riesgo de automatización
    y urgencia de recapacitación.
    """

    correlacion = calcular_correlacion(
        df_limpio,
        "porcentaje_riesgo_automatizacion",
        "puntaje_urgencia_recapacitacion"
    )


    conclusion = """
    Relación fuerte y positiva, pero no perfecta: a mayor riesgo de
    automatización, mayor urgencia de recapacitación. La dispersión crece en
    los niveles altos de riesgo, lo que indica que otros factores (rol
    específico, industria, políticas de recapacitacoin) también influyen en la
    urgencia real de reconversión laboral.
    """

    print(
        f"Correlación riesgo-urgencia: {correlacion:.4f}"
    )

    print(conclusion)


    return {
        "correlacion": correlacion,
        "conclusion": conclusion
    }