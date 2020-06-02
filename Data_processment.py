import numpy as np
import pandas as pd


def createFile ():
    with open("Dados/Dados.csv", "r") as file:
        Header = file.readline()
        Data = file.readlines()
        
    Rows = 0
    for char in Header:
        if char == ";":
            Rows = Rows + 1
    

    with open("Dados/Dados Processados.csv", "w") as file:
        file.write(Header)
        actualLine = ""
        CountRows = 0
        for line in Data:
            actualLine = actualLine + line
            for char in line:
                if char == ";":
                    CountRows = CountRows + 1
            # print(CountRows, actualLine)
            if CountRows == Rows:
                actualLine = actualLine.replace("\n","") + "\n"
                file.write(actualLine)
                actualLine = ""
                CountRows = 0


# createFile()
csv_path = "Dados/Dados Processados.csv"
df = pd.read_csv(csv_path)
print(df.head())