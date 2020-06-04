import numpy as np
import mysql.connector
import pickle

def readMask():
    #POI rows and columns categories
    mask = np.load('mask.npy')

    return mask


#def readMatrix(group_ID, listIDUsers):
def readMatrix():
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    group_ID = 8339837

    listIDUsers = [39, 41, 42]

    try:

        with open('listaIDPOI.pkl', 'rb') as f:
            listaIDPOI = pickle.load(f)
            f.close()

        sql = """SELECT userID, POI_ID, rate FROM ratings WHERE group_ID = '%s'""" % (group_ID)
        cursor.execute(sql)
        results = cursor.fetchall()


        matrix = np.zeros((len(listIDUsers), len(listaIDPOI)), dtype=np.float)

        print(len(listaIDPOI))
        print(matrix)

        # for row in results:
        #     IDuser = row[0]
        #     POI_ID = row[1]
        #     rate = row[2]
        #
        #     matrix[listIDUsers.index(IDuser)][listaIDPOI.index(POI_ID)] = ((0.5) * rate) / 5

    except:
        pass

    return matrix

m= readMatrix()
