from modulos.carga import cargar_datos

from modulos.auditoria_inicial import auditar_calidad

from modulos.limpieza import limpiar_dataset
from modulos.traduccion import traducir_df

from modulos.analisis_estabilidad_salarial import analizar_estabilidad_salarial

from modulos.analisis_tendencias_demanda import analizar_tendencias_demanda

from modulos.analisis_niveles_riesgo import analizar_niveles_riesgo

from modulos.analisis_top_10 import calcular_top10_manufactura, interpretar_top10_manufactura
from modulos.graficos import graficar_top10_manufactura

from modulos.analisis_frecuencias_salarios import analizar_distribucion_salarios, interpretar_distribucion_salarios
from modulos.graficos import graficar_histograma_salarios

from modulos.analisis_brecha_automatizacion import analizar_brecha_vs_riesgo, analizar_riesgo_vs_urgencia
from modulos.graficos import graficar_scatter_brecha_riesgo, graficar_scatter_muestra, graficar_scatter_riesgo_urgencia

from modulos.reflexion_fabrica_sin_humanos import generar_reflexion_fabrica_sin_humanos

from modulos.reflexion_paises import construir_tabla_paises_manufactura, interpretar_tabla_paises_manufactura

from modulos.graficos import graficar_tendencia_demanda


def main():

    # 1. CARGA DE DATOS
    print("""
        ============================================================
        CARGA DE DATOS
        ============================================================
        """)

    df = cargar_datos("datos/ai_job_replacement_dirty.csv")


    # 2. FASE I — AUDITORÍA DE CALIDAD
    print("""
        ============================================================
        AUDITORÍA DE CALIDAD — Estado inicial del dataset
        ============================================================
        """)

    auditoria_inicial = auditar_calidad(df)
    print(auditoria_inicial)


    # 3. FASE I — PROTOCOLO DE CURACIÓN Y TRADUCCION
    print("""
        ============================================================
        FASE I — PROTOCOLO DE CURACIÓN Y TRADUCCION
        ============================================================
        """)

    df_limpio_sin_traducir = limpiar_dataset(df)
    df_limpio = traducir_df(df_limpio_sin_traducir)

    df_manufactura = df_limpio[df_limpio["industria"] == "Manufactura"].copy()

    print(df_limpio.info())
    print(df_limpio.describe())
    print("Dataset limpio!")


    # 4. FASE II — ESTABILIDAD SALARIAL: Calculen la media y la mediana de los salarios. 
    # Expliquen la importancia de usar ambas métricas en presencia de valores atípicos detectados.

    print("""
        ============================================================
        FASE II — ESTABILIDAD SALARIAL
        ============================================================
        """)

    resultado_estabilidad_salarial = analizar_estabilidad_salarial(df_limpio,df_manufactura)
    resultado_estabilidad_salarial


    # 5. FASE II — TENDENCIAS DE DEMANDA DE HABILIDADES: 
    # Analicen el crecimiento promedio de la demanda de habilidades por año. 
    # ¿Se está acelerando la necesidad de perfiles híbridos?

    print("""
        ============================================================
        FASE II — TENDENCIAS DE DEMANDA DE HABILIDADES
        ============================================================
        """)

    resultado_tendencias_demanda = analizar_tendencias_demanda(df_limpio,df_manufactura)

    graficar_tendencia_demanda(resultado_tendencias_demanda["global"], "Tendencia global de habilidades", "tendencia_global_habilidades")
    graficar_tendencia_demanda(resultado_tendencias_demanda["manufactura"],"Tendencia habilidades Manufactura","tendencia_manufactura_habilidades")


    # 6. FASE II — NIVELES DE RIESGO: 
    # Determinen qué porcentaje de los trabajadores de manufactura se encuentran en la categoría de "Alto Riesgo".

    print("""
        ============================================================
        FASE II — NIVELES DE RIESGO
        ============================================================
        """)

    resultado_niveles_riesgo = analizar_niveles_riesgo(df_limpio, df_manufactura)
    resultado_niveles_riesgo


    # 7. FASE III — GRÁFICO: TOP 10 ROLES DE MANUFACTURA POR RIESGO: 
    # Grafico de Barras Horizontales: Los 10 puestos de manufactura con mayor ai_replacement_score

    print("""
        ============================================================
        FASE III — GRÁFICO: TOP 10 ROLES DE MANUFACTURA POR RIESGO
        ============================================================
        """)

    top10_manufactura = calcular_top10_manufactura(df_manufactura)

    graficar_top10_manufactura(top10_manufactura)

    conclusion_top_10 = interpretar_top10_manufactura(top10_manufactura)
    print(conclusion_top_10)


    # 8. FASE III — GRÁFICO: HISTOGRAMA DE SALARIOS POR INDUSTRIA: 
    # Histograma de Salarios: Distribución de frecuencias de los salarios post-IA en la industria.

    print("""
        ============================================================
        FASE III — GRÁFICO: HISTOGRAMA DE SALARIOS POR INDUSTRIA
        ============================================================
        """)

    resultado_salarios = analizar_distribucion_salarios(df_limpio)

    print("\n--- Distribución salarial ---")
    print(f"Media salarial: USD {resultado_salarios['media']:.2f}")
    print(f"Mediana salarial: USD {resultado_salarios['mediana']:.2f}")
    print(f"Bins óptimos (Freedman-Diaconis): {resultado_salarios['bins']}")

    print(interpretar_distribucion_salarios())

    graficar_histograma_salarios(df_limpio,resultado_salarios["bins"])


    # 9. FASE III — SCATTER: BRECHA DE HABILIDADES VS. RIESGO 
    # Scatter Plot: Relación entre el índice de brecha de habilidades y el riesgo de automatización.

    print("""
        ============================================================
        FASE III — SCATTER: BRECHA DE HABILIDADES VS. RIESGO
        ============================================================
        """)

    resultado_brecha = analizar_brecha_vs_riesgo(df_limpio)
    resultado_brecha
    graficar_scatter_brecha_riesgo(df_limpio,"scatter_habilidades_riesgo.png")

    print(resultado_brecha["muestra"])
    graficar_scatter_muestra(resultado_brecha["muestra"])

    resultado_urgencia = analizar_riesgo_vs_urgencia(df_limpio)
    resultado_urgencia
    graficar_scatter_riesgo_urgencia(df_limpio)


    # 10. FASE IV — REFLEXIÓN CRÍTICA 
    # ¿La IA está impulsando una "fábrica sin humanos" o una fábrica de "empleados premium"?

    print("""
        ============================================================
        FASE IV — REFLEXIÓN CRÍTICA
        ============================================================
        """)

    reflexion_fabrica_sin_humanos = generar_reflexion_fabrica_sin_humanos(resultado_estabilidad_salarial,resultado_niveles_riesgo)
    print(reflexion_fabrica_sin_humanos)


    # 11. FASE IV — TABLA COMPARATIVA POR PAÍS (MANUFACTURA) 
    # ¿Qué país del dataset parece haber gestionado mejor la transición a la IA en manufactura según la evolución salarial?
    
    print("""
    ============================================================
    ¿Qué país del dataset parece haber gestionado mejor la transición a la IA en manufactura según la evolución salarial?
    ============================================================
    """)

    tabla_paises = construir_tabla_paises_manufactura(df_manufactura)
    print("\n--- Evolución salarial por país ---")
    print(tabla_paises)
    print(interpretar_tabla_paises_manufactura(tabla_paises))


if __name__ == "__main__":
    main()
