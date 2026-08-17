def traducir_columnas(df_traducido):
    df_traducido.rename(columns={
        'job_id': 'id_trabajo', 'job_role': 'rol_laboral', 'industry': 'industria',
        'country': 'pais', 'year': 'año',
        'automation_risk_percent': 'porcentaje_riesgo_automatizacion',
        'ai_replacement_score': 'puntaje_reemplazo_ia',
        'skill_gap_index': 'indice_brecha_habilidades',
        'salary_before_usd': 'salario_antes_usd', 'salary_after_usd': 'salario_despues_usd',
        'salary_change_percent': 'porcentaje_cambio_salario',
        'skill_demand_growth_percent': 'porcentaje_crecimiento_demanda_habilidades',
        'remote_feasibility_score': 'puntaje_factibilidad_remoto',
        'ai_adoption_level': 'nivel_adopcion_ia',
        'education_requirement_level': 'nivel_requisito_educativo',
        'automation_risk_category': 'categoria_riesgo_automatizacion',
        'skill_transition_pressure': 'presion_transicion_habilidades',
        'wage_volatility_index': 'indice_volatilidad_salario',
        'reskilling_urgency_score': 'puntaje_urgencia_recapacitacion',
        'ai_disruption_intensity': 'intensidad_disrupcion_ia',
    }, inplace=True)


def traducir_riesgo_automatizacion(df_traducido):
    mapa_riesgo = {'Low': 'Bajo', 'Medium': 'Medio', 'High': 'Alto'}
    df_traducido['categoria_riesgo_automatizacion'] = (
        df_traducido['categoria_riesgo_automatizacion'].map(mapa_riesgo)
    )

def traducir_industria(df_traducido):
    mapa_industria = {
        'Technology': 'Tecnología', 'Finance': 'Finanzas', 'Manufacturing': 'Manufactura',
        'Healthcare': 'Salud', 'Retail': 'Retail', 'Education': 'Educación',
        'Transportation': 'Transporte', 'Energy': 'Energía',
    }
    df_traducido['industria'] = df_traducido['industria'].map(mapa_industria)

def traducir_rol_laboral(df_traducido):
    mapa_rol_laboral = {
        'Marketing Specialist': 'Especialista en marketing', 'Teacher': 'Maestro',
        'Data Analyst': 'Analista de datos', 'Mechanical Engineer': 'Ingeniero mecanico',
        'Customer Support Rep': 'Representante de atención al cliente',
        'HR Manager': 'Gerente de Recursos Humanos', 'Truck Driver': 'Conductor de camion',
        'Software Engineer': 'Ingeniero de software', 'Financial Analyst': 'Analista financiero',
        'Accountant': 'Contador',
    }
    df_traducido['rol_laboral'] = df_traducido['rol_laboral'].map(mapa_rol_laboral)

def traducir_paises(df_traducido):
    mapa_paises = {
        'Singapore': 'Singapur', 'USA': 'EEUU', 'Brazil': 'Brasil',
        'Japan': 'Japon', 'Germany': 'Alemania',
    }
    df_traducido['pais'] = df_traducido['pais'].replace(mapa_paises)

def traducir_df(df_limpio):
    """
    Renombra las columnas al español y traduce los valores de las
    columnas categóricas (industria, riesgo, rol laboral, país).

    Devuelve un nuevo DataFrame (no modifica el de entrada).
    """
    df_traducido = df_limpio.copy()

    traducir_columnas(df_traducido)
    traducir_riesgo_automatizacion(df_traducido)
    traducir_industria(df_traducido)
    traducir_rol_laboral(df_traducido)
    traducir_paises(df_traducido)

    return df_traducido