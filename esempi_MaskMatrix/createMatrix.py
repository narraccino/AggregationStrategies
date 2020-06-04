import mysql.connector
import pandas as pd
import traceback
import numpy as np
from sklearn import preprocessing

db = mysql.connector.connect(user='mattarella', password='mattarella',
                             host='127.0.0.1',
                             database='dbaggregationstrategies')

# prepare a cursor object using cursor() method
cursor = db.cursor()

group_ID = 8339837
userID= 39

listUsers=[39,41,42]


try:

    sql = """SELECT POI_ID FROM ratings WHERE userID = '%s'""" % (userID)
    cursor.execute(sql)
    results = cursor.fetchall()
    listaIDPOI= [row[0] for row in results]




    sql = """SELECT userID, POI_ID, rate FROM ratings WHERE group_ID = '%s'""" % (group_ID)
    cursor.execute(sql)
    results = cursor.fetchall()
    #print(results)



    matrix = np.zeros((len(listUsers), len(listaIDPOI)), dtype=np.float)



    for row in results:
        IDuser = row[0]
        POI_ID = row[1]
        rate = row[2]

        matrix[listUsers.index(IDuser)][listaIDPOI.index(POI_ID)] = rate

except:
    pass

print(matrix[0])


min_max_scaler = preprocessing.MinMaxScaler()
for i in range(len(matrix)):
    matrix[i] = min_max_scaler.fit_transform(matrix[i].reshape(-1,1)).reshape(1,10)
print(matrix)