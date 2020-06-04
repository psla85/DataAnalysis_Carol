import pandas as pd
from replacements import lowerCases


def countLocations(Data):

    dataArray = []
    for line in Data:
        line = line.title()
        line = line.strip("\"\n ")
        for tup in lowerCases:
            line = line.replace(tup[0], tup[1])
        Arr = line.split(", ")
        dataArray.append(Arr)

    location = []
    qntd = []
    for row in dataArray:
        for item in row:
            if item in location:
                qntd[location.index(item)] = qntd[location.index(item)] + 1
            else:
                location.append(item)
                qntd.append(1)

    output = []
    for i, item in enumerate(location):
        output.append((item, qntd[i]))

    return output


def alphaOrder(Data):

    location = []
    for tup in Data:
        location.append(tup[0])
    location.sort()

    output = []
    for item in location:
        for tup in Data:
            if item == tup[0]:
                output.append(tup)
                break

    return output


def qntdOreder(Data):
    copyData = Data.copy()
    qntd = []
    for tup in Data:
        qntd.append(tup[1])
    qntd.sort(reverse=True)

    output = []
    for item in qntd:
        for tup in copyData:
            if item == tup[1]:
                output.append(tup)
                copyData.remove(tup)
                break

    return output


def createCSV(path, name):
    path_csvInput = path + "/Referencia/" + name + ".csv"

    with open(path_csvInput, "r", encoding="UTF8") as file:
        Data = file.readline()
        Data = file.readlines()

    count = countLocations(Data)
    Alpha = alphaOrder(count)
    qntd = qntdOreder(Alpha)

    lengthIndex = list(range(1, len(count) + 1))
    Columns = ["Cidade", "Quantidade de Menções"]

    df = pd.DataFrame(count, columns=Columns, index=lengthIndex)
    df_Alpha = pd.DataFrame(Alpha, columns=Columns, index=lengthIndex)
    df_qntd = pd.DataFrame(qntd, columns=Columns, index=lengthIndex)

    df.to_csv(path + "/" + name + " - Citados.txt",
              encoding="utf8", sep=";")
    df_Alpha.to_csv(path + "/" + name +
                    " - Ordem Alfabética.txt", encoding="utf8", sep=";")
    df_qntd.to_csv(path + "/" + name +
                   " - Oredem Quantidade.txt", encoding="utf8", sep=";")


createCSV("Dados", "Visitados")
createCSV("Dados", "Indicacao")
createCSV("Dados", "Interesse")
