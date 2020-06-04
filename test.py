import pandas as pd


count = [[1, 1], [2, 2], [3, 3], [4, 4]]
df = pd.DataFrame(count)
print(df)

df.to_excel("Teste.xlsx")
