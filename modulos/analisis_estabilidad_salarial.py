def calcular_estadisticas_salariales(df):
    """
    Calcula media y mediana de salarios antes y después de IA.
    """

    return {
      "media_antes": df["salario_antes_usd"].mean(),
      "mediana_antes": df["salario_antes_usd"].median(),
      "media_despues": df["salario_despues_usd"].mean(),
      "mediana_despues": df["salario_despues_usd"].median()
    }


def imprimir_estadisticas_salariales(nombre, estadisticas):
    """
    Muestra por pantalla las estadísticas calculadas.
    """

    print(f"\nSalario Antes IA ({nombre}) -> "
          f"Media: USD {estadisticas['media_antes']:.2f} | "
          f"Mediana: USD {estadisticas['mediana_antes']:.2f}")

    print(f"Salario Después IA ({nombre}) -> "
          f"Media: USD {estadisticas['media_despues']:.2f} | "
          f"Mediana: USD {estadisticas['mediana_despues']:.2f}")


def analizar_estabilidad_salarial(df_limpio, df_manufactura):
      """
      Compara estabilidad salarial general y en Manufactura.
      """

      # Dataset completo
      estadisticas_general = calcular_estadisticas_salariales(df_limpio)

      imprimir_estadisticas_salariales("Dataset completo", estadisticas_general)

      print("""
            Análisis (Dataset completo):
            La media sube levemente tras la IA, mientras que la mediana baja. Esta
            divergencia es un síntoma de polarización salarial: un grupo reducido de
            roles experimenta incrementos considerables que arrastran la media hacia
            arriba, mientras que el trabajador típico (mediana) sufre una leve pérdida
            de poder de negociación salarial.
      """)


      # Manufactura
      estadisticas_manufactura = calcular_estadisticas_salariales(df_manufactura)

      imprimir_estadisticas_salariales("Manufactura", estadisticas_manufactura)

      caida_mediana_general = (estadisticas_general["mediana_antes"] - estadisticas_general["mediana_despues"])
      caida_mediana_manufactura = (estadisticas_manufactura["mediana_antes"] - estadisticas_manufactura["mediana_despues"])

      print(f"""
            Análisis (Manufactura):
            Se repite el mismo patrón de divergencia: la media sube (+{estadisticas_manufactura["media_despues"] - estadisticas_manufactura["media_antes"]:.2f} USD)
            mientras la mediana baja (-{caida_mediana_manufactura:.2f} USD). La caída de la mediana en
            Manufactura es {caida_mediana_manufactura / caida_mediana_general:.2f} veces mayor que la caída
            general del dataset (-{caida_mediana_general:.2f} USD), lo que sugiere que la polarización
            salarial se manifiesta de forma más intensa dentro de este sector.
      """)

      return {
            "general": estadisticas_general,
            "manufactura": estadisticas_manufactura
      }