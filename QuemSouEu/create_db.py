import pandas as pd
import openpyxl

df = pd.DataFrame(data=[["Diego", 50]], columns=['Nome', 'Pontuação'])

df.to_excel("Pontuacoes.xlsx")
