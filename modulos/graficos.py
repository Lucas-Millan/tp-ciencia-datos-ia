import matplotlib.pyplot as plt
import seaborn as sns


def graficar_tendencia_demanda(
        tendencia,
        titulo,
        nombre_archivo):

    plt.figure()

    sns.lineplot(
        x="año",
        y="porcentaje_crecimiento_demanda_habilidades",
        data=tendencia,
        marker="o",
        linewidth=2
    )

    plt.xlabel("Año")
    plt.ylabel(
        "Crecimiento promedio de demanda de habilidades (%)"
    )

    plt.title(titulo)

    plt.grid(
        axis="both",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        f"resultados/{nombre_archivo}.png",
        dpi=150
    )

    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns


def graficar_top10_manufactura(top10):
    """
    Genera gráfico de barras horizontales
    de riesgo de reemplazo por IA.
    """

    plt.figure(figsize=(9, 6))

    sns.barplot(
        data=top10,
        x="puntaje_reemplazo_ia",
        y="rol_laboral"
    )

    plt.xlabel(
        "Puntaje de reemplazo por IA (promedio)"
    )

    plt.ylabel(
        "Rol laboral"
    )

    plt.title(
        "Puestos de Manufactura por riesgo de reemplazo por IA"
    )

    plt.grid(
        axis="both",
        alpha=0.3
    )


    for i, valor in enumerate(
        top10["puntaje_reemplazo_ia"]
    ):
        plt.text(
            valor + 0.5,
            i,
            f"{valor:.1f}",
            va="center"
        )


    plt.tight_layout()

    plt.savefig(
        "resultados/top10_manufactura.png",
        dpi=150
    )

    plt.show()



def graficar_histograma_salarios(df_limpio, bins):
    """
    Genera histogramas de salarios post IA.
    """

    # Histograma general

    plt.figure(figsize=(9,6))

    sns.histplot(
        data=df_limpio,
        x="salario_despues_usd",
        bins=40
    )


    plt.axvline(
        df_limpio["salario_despues_usd"].mean(),
        linestyle="--",
        label="Media"
    )


    plt.axvline(
        df_limpio["salario_despues_usd"].median(),
        linestyle="--",
        label="Mediana"
    )


    plt.xlabel("Salario post IA (USD)")
    plt.ylabel("Frecuencia")
    plt.title(
        "Distribución de salarios post-IA"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "resultados/histograma_salarios_general.png",
        dpi=150
    )

    plt.show()


    # Comparativo por industria

    plt.figure(figsize=(10,6))

    sns.histplot(
        data=df_limpio,
        x="salario_despues_usd",
        hue="industria",
        bins=bins,
        element="step",
        stat="density",
        common_norm=False
    )


    plt.xlim(0,200000)

    plt.xlabel("Salario post IA (USD)")
    plt.ylabel("Densidad")

    plt.title(
        "Distribución de salarios post-IA por industria"
    )

    plt.tight_layout()

    plt.savefig(
        "resultados/histograma_industrias.png",
        dpi=150
    )

    plt.show()

def graficar_scatter_brecha_riesgo(df_limpio, nombre_archivo):

    sns.scatterplot(
        data=df_limpio,
        x="indice_brecha_habilidades",
        y="porcentaje_riesgo_automatizacion"
    )

    plt.xlabel(
        "Índice de brecha de habilidades"
    )

    plt.ylabel(
        "Porcentaje de riesgo de automatización"
    )

    plt.title(
        "Brecha de habilidades vs Riesgo de automatización"
    )


    plt.tight_layout()

    plt.savefig(
        "resultados/scatter_habilidades_riesgo.png",
        dpi=150
    )

    plt.show()

def graficar_scatter_muestra(muestra):

    sns.scatterplot(
        data=muestra,
        x="indice_brecha_habilidades",
        y="porcentaje_riesgo_automatizacion",
        alpha=0.6
    )

    plt.title(
        "Brecha vs Riesgo (muestra n=1000)"
    )

    plt.tight_layout()

    plt.savefig(
        "resultados/scatter_muestra.png",
        dpi=150
    )

    plt.show()


def graficar_scatter_riesgo_urgencia(df_limpio):

    sns.scatterplot(
        data=df_limpio,
        x="porcentaje_riesgo_automatizacion",
        y="puntaje_urgencia_recapacitacion",
        alpha=0.3
    )


    plt.xlabel(
        "Riesgo de automatización (%)"
    )

    plt.ylabel(
        "Urgencia de recapacitación"
    )

    plt.title(
        "Riesgo vs Urgencia de recapacitación"
    )


    plt.tight_layout()

    plt.savefig(
        "resultados/scatter_riesgo_urgencia.png",
        dpi=150
    )

    plt.show()