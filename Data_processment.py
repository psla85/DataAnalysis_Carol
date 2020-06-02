import numpy as np
import pandas as pd


def createFile():
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
                actualLine = actualLine.replace("\n", ",")
                actualLine = actualLine[:-1] + "\n"
                file.write(actualLine)
                actualLine = ""
                CountRows = 0


def checkRepetedRows(df):

    lines = []
    repeted = []
    rows, cols = df.shape
    print(rows, cols)
    line = ""

    for row in range(4):
        for col in range(1, cols):
            line = line + str(df.iloc[row, col])
        lines.append(line)
        line = ""
    print(len(lines), lines)

    # if lines[2] == lines[3]:
    #     print("Igual")
    # else:
    #     print("Diferente")

    for i, row_i in enumerate(line):
        for j, row_j in enumerate(lines):
            if j > i and row_i == row_j:
                repeted.append(i)
                break

    with open("Dados/Repetidos.csv", "w") as file:
        for i in repeted:
            file.write(i)


# createFile()
csv_path = "Dados/Dados Processados.csv"
df = pd.read_csv(csv_path, sep=";", encoding='latin-1')

# df["Visitados"].to_csv("Dados/Visitados.csv", index=False)
# df["Interesse"].to_csv("Dados/Interesse.csv", index=False)
# df["Indicacao"].to_csv("Dados/Indicacao.csv", index=False)
# cities_1 = df["Visitados"]
# cities_2 = df["Interesse"]
# cities_3 = df["Indicacao"]

checkRepetedRows(df)
