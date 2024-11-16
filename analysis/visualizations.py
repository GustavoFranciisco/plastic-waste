import os
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(data):
    
    # Criando visualizações a partir dos dados processados
    
    # Criar o diretório 'output'
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Selecionando toop 10 países que geram mais resíduos plásticos
    top_countries = data.groupby('country')['plastic_generated'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index)
    plt.title('Top 10 Países que Geram Mais Resíduos Plásticos (Toneladas)')
    plt.xlabel('Quantidade de Resíduos Gerados (Toneladas)')
    plt.ylabel('País')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_10_countries_plastic_generated.png'))
    plt.show()

    # Correlação entre taxa de reciclagem e resíduos mal gerenciados
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='recycling_rate', y='plastic_generated', hue='country', legend=False)
    plt.title('Correlação entre Taxa de Reciclagem e Resíduos Plásticos Gerados')
    plt.xlabel('Taxa de Reciclagem (%)')
    plt.ylabel('Resíduos Gerados (Toneladas)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'recycling_vs_generated.png'))
    plt.show()
