from allredemption import allredemption


def processallredemption():
    redemptionList =[]
    allredemption_file = open("file/allredemption.txt", "r")
    for i in  allredemption_file:
        list = i.split(',')
        s = allredemption(list[0], list[1], list[2], list[3], int(list[4]),list[5], list[6])
        redemptionList.append(s)
    return redemptionList
