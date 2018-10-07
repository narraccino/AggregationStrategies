import csv

def prepareTableCSV(listName):
    with open('C:/Users/neo/Desktop/rankings.csv', 'w') as csvfile:
        len_Names = len(listName)
        fieldnames=[]
        for i in range(0,len_Names):
            fieldnames.append(listName[i])

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

def saveUserRankings(rankingsArrayPOI, listPOI):
    with open('C:/Users/neo/Desktop/rankings.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

