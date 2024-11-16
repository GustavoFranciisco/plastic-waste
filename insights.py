def generate_insights(data):
 
    #Analisa os dados e gera insights

    # País com maior geração de resíduos
    max_generated = data.loc[data['plastic_generated'].idxmax()]
    print(f"O país com maior geração de resíduos plásticos é {max_generated['country']} com {max_generated['plastic_generated']} toneladas.")

    # País com maior taxa de reciclagem
    max_recycling = data.loc[data['recycling_rate'].idxmax()]
    print(f"O país com a maior taxa de reciclagem é {max_recycling['country']} com {max_recycling['recycling_rate']}%.")

    # Removendo análise de plastic_mismanaged, pois a coluna não existe
    print("Análise de resíduos mal gerenciados não foi realizada porque a coluna não está presente no dataset.")
