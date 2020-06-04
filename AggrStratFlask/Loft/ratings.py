from json.decoder import NaN
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
