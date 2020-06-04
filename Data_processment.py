import os
import numpy as np
import pandas as pd
from replacements import repList, repIterList


def createFile(path_1, path_2):
    with open(path_1, "r", encoding="UTF8") as file:
        Header = file.readline()
        Data = file.readlines()

    Cols = 0
    for char in Header:
        if char == ";":
            Cols = Cols + 1
    print("Columns", Cols)

    with open(path_2, "w", encoding="UTF8") as file:
        # Header = Header.replace("\"", "")
        file.write(Header)
        actualLine = ""
        CountCols = 0
        for line in Data:
            actualLine = actualLine + line
            for char in line:
                if char == ";":
                    CountCols = CountCols + 1
            if CountCols == Cols:
                actualLine = actualLine.replace("\"", "")
                actualLine = actualLine.replace("\n", ",")
                actualLine = actualLine[:-1] + "\n"
                file.write(actualLine)
                actualLine = ""
                CountCols = 0


def checkRepetedRows(path_1, path_2):

    df = pd.read_csv(path_1, sep=";", encoding="utf8")
    lines = []
    repeted = []
    rows, cols = df.shape
    line = ""

    for row in range(rows):
        for col in range(1, cols):
            line = line + str(df.iloc[row, col])
        lines.append(line)
        line = ""

    for i, row_i in enumerate(lines):
        for j, row_j in enumerate(lines):
            if j > i and row_i == row_j:
                repeted.append(j)
                break

    repeted = sorted(repeted)

    with open(path_2, "w", encoding="UTF8") as file:
        for i in repeted:
            add = "\n"
            if i == repeted[-1]:
                add = ""
            file.write(str(i) + add)


def deleteRepeted(path_1, path_2):
    with open(path_1, "r", encoding="UTF8") as file:
        Header = file.readline()
        Data = file.readlines()

    with open(path_2, "r", encoding="UTF8") as file:
        repeted = file.readlines()

    j = 0
    os.remove(path_1)
    with open(path_1, "w", encoding="UTF8") as file:
        file.write(Header)
        for i, line in enumerate(Data):
            if i == int(repeted[j]):
                j = j + 1
            else:
                file.write(line)

            if j == len(repeted):
                break


def initiateData(path):
    path_data = path + "/Referencia/Dados.csv"
    path_processed = path + "/Dados Processados.csv"
    path_repeted = path + "/Repetidos.csv"
    createFile(path_data, path_processed)
    print("1")
    checkRepetedRows(path_processed, path_repeted)
    print("2")
    deleteRepeted(path_processed, path_repeted)
    print("3")


def cleanData(path, df, name):

    dataFrame = df[name]
    dataFrame.to_csv(path + "/" + name + " antes.csv",
                     index=False, encoding="utf8")
    err = []
    list = []
    for i, item in enumerate(dataFrame):
        for rep in repList:
            item = item.replace(rep[0], rep[1])
        for rep in repIterList:
            while rep[0] in item:
                item = item.replace(rep[0], rep[1])
        item = item.strip("/,.- ")
        list.append(item)
        count = 0
        for char in item:
            if char == ",":
                count = count + 1
        if count < 4:
            err.append(i+2)
    new_df = pd.DataFrame(list, columns=[name])
    print(len(err))
    print(err)
    new_df.to_csv(path + "/" + name + ".csv",
                  index=False, encoding="utf8")


def separete(path, rang):
    df = pd.read_csv(path + "/Dados Processados.csv",
                     sep=";", encoding='utf8')
    names = df.columns
    for i in rang:
        cleanData(path, df, names[i])


print("start")

csv_path = "Dados"
# initiateData(csv_path)
# separete(csv_path, [2, 3])

print("done")
