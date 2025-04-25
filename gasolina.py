
import pandas as pd
import seaborn as sns
import matplotlib as plt

gasolina_df = pd.read_csv("gasolina.csv", sep=",")
gasolina_df.head()

with sns.axes_style('whitegrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x="dia", y="venda", marker='o', color='red')
  grafico_gasolina.set(title='Custo da gasolina em São Paulo-SP em Julho/2021', xlabel='data', ylabel='custo')
  grafico_gasolina.figure.savefig("gasolina.png", dpi=300)
