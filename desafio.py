import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo Excel
caminho_arquivo_excel = 'caminho/do/seu/arquivo/exemplo.xlsx'
dados = pd.read_excel(caminho_arquivo_excel)

# Visualizar as primeiras linhas dos dados
print("Primeiras 5 linhas dos dados:")
print(dados.head())

# Informações sobre o conjunto de dados
print("\nInformações sobre o conjunto de dados:")
print(dados.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(dados.describe())

# Visualização de dados temporais (se houver coluna de datas)
if 'Data' in dados.columns:
    # Converter a coluna 'Data' para o tipo datetime
    dados['Data'] = pd.to_datetime(dados['Data'])

    # Visualizar dados temporais
    plt.figure(figsize=(10, 6))
    plt.plot(dados['Data'], dados['Valor'], marker='o')
    plt.title('Visualização de Dados Temporais')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.show()

# Análise exploratória (exemplo de histograma)
dados['Valor'].plot(kind='hist', bins=20, edgecolor='black', figsize=(10, 6))
plt.title('Histograma de Valores')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()
