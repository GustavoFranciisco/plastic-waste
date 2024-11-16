def clean_data(data):

    #Limpando e pré-processamento dos dados.
    
    # Colunas a serem mantidas
    columns_to_keep = [
        'Country', 
        'Total_Plastic_Waste_MT', 
        'Recycling_Rate'
    ]
    data = data[columns_to_keep].copy()  # Cria uma cópia

    # Renomear colunas para facilitar o entendimento
    data.rename(columns={
        'Country': 'country',
        'Total_Plastic_Waste_MT': 'plastic_generated',
        'Recycling_Rate': 'recycling_rate'
    }, inplace=True)

    # Tratando valores nulos
    data.dropna(inplace=True)

    # Verificar dados duplicados
    data.drop_duplicates(inplace=True)

    print(f"Dados limpos: {data.shape[0]} linhas e {data.shape[1]} colunas.")
    return data
