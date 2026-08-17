def generar_reflexion_fabrica_sin_humanos(estabilidad_salarial, niveles_riesgo):
    """
    Genera la reflexión final sobre la hipótesis de "fábrica sin humanos"
    utilizando resultados obtenidos previamente.
    """

    manuf = estabilidad_salarial["manufactura"]

    caida_mediana = (
        manuf["mediana_antes"] -
        manuf["mediana_despues"]
    )


    porcentaje_alto_riesgo = (
        niveles_riesgo["riesgo_manufactura"]
        .get("Alto", 0)
    )


    reflexion = f"""
        ============================================================
        ¿"Fábrica sin humanos" o fábrica de "empleados premium"?
        ============================================================

        Los datos respaldan la hipótesis de "empleados premium",
        no la de "fábrica sin humanos".

        - La media salarial en Manufactura aumenta levemente,
        pero la mediana cae ({caida_mediana:.2f} USD).
        Esto evidencia una polarización salarial: algunos roles
        capturan beneficios mientras otros pierden poder salarial.

        - El {porcentaje_alto_riesgo:.2f}% de trabajadores se encuentra
        en categoría de Alto Riesgo. Es una proporción relevante,
        pero no representa una desaparición generalizada del empleo.

        Si la narrativa fuera "fábrica sin humanos", esperaríamos una
        caída salarial generalizada y una mayoría de trabajadores en
        alto riesgo. Los datos no muestran ese patrón.

        En cambio, aparece una coexistencia entre trabajadores que
        obtienen beneficios de la incorporación de IA y otros que
        enfrentan mayor vulnerabilidad.
        """

    return reflexion