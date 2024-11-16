import pandas as pd
from analysis.data_cleaning import clean_data
from analysis.visualizations import create_visualizations
from analysis.insights import generate_insights

def main():
    print("=== Global Plastic Waste 2023 Analysis ===")
    
    # Carregar dados
    print("Carregando dados...")
    data = pd.read_csv('data/plastic_waste_2023.csv')

    # Limpeza e pré-processamento
    print("Limpando e processando os dados...")
    cleaned_data = clean_data(data)

    # Gerar visualizações
    print("Criando visualizações...")
    create_visualizations(cleaned_data)

    # Gerar insights
    print("Analisando padrões...")
    generate_insights(cleaned_data)

if __name__ == "__main__":
    main()
