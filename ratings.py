from json.decoder import NaN
# from saveData import prepareTableCSV
# from saveData import saveUserRankings

import numpy as np

def first_rate(username, listPOI, listCat):
    # len_Names= len(listName)
    len_POI = len(listPOI)
    # ratingsArrayPOI= np.zeros(len_POI)
    ratingsArrayPOI=list()



    print('\n\n\nHey ',username,', rate these POIs : \n\n' )
    for j in range(0, len_POI):
        print(listPOI[j], ' (category: ', listCat[j],')', '\n')
        rate= int(input('Rate this POI (1-10) or NA: ---->'))
        ratingsArrayPOI.append(rate)
        #print(type(ratingsArrayPOI))
        print('\n')

    return ratingsArrayPOI
        #saveUserRankings(rankingsArrayPOI, listPOI)

    # print("Name")
    # for i in range(0, len_POI):
    #     print(listPOI[i])
    #
    # print('\n\n')
    # for i in range(0,len_Names):
    #         print(listName[i])
    #         for j in range(0, len_POI):
    #             print(int(ratingsArrayPOI[i][j]))
    #         print('\n\n')

