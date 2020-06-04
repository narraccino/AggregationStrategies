import mysql.connector
import pandas as pd
import traceback
import numpy as np


listaPOI= [11,12,13,14]

print(listaPOI.index(13))

mask= np.zeros((len(listaPOI),len(listaPOI)), dtype=np.float32)

mask[2][3]=1

print(mask)


# from sklearn import preprocessing
#
# db = mysql.connector.connect(user='mattarella', password='mattarella',
#                              host='127.0.0.1',
#                              database='dbaggregationstrategies')
#
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
#
# group_ID = 8339837
# userID= 39
#
# listUsers=[39,41,42]
#
#
# try:
#     sql = """SELECT POI_ID FROM ratings WHERE userID = '%s'""" % (userID)
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     #print(results)
#     lista= [row[0] for row in results ]
#     df = pd.DataFrame(index=listUsers, columns=lista, data= 0)
#     #print(df)
#
#     sql = """SELECT userID, POI_ID, rate FROM ratings WHERE group_ID = '%s'""" % (group_ID)
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         IDuser = row[0]
#         POI_ID = row[1]
#         rate = row[2]
#         df.loc[IDuser, POI_ID]= ((0.5)*rate)/5
#
#     #print(df)
#
#     sql = """SELECT * FROM occurrences WHERE 1"""
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     listaIDPOI = [row[0] for row in results]
#     listaIDCAT = [row[1] for row in results]
#
#     df_Mask = pd.DataFrame(index=listaIDPOI, columns=listaIDCAT, data=0)
#
#     for row in results:
#         df_Mask.loc[row[0], row[1]] = 1
#
#     #print(df_Mask)
#
#
# except:
#     traceback.print_exc()
#
#
#
# df.to_pickle("./df.pkl")
# df_Mask.to_pickle("./df_Mask.pkl")
#
# a= pd.read_pickle("./df.pkl")
# b= pd.read_pickle("./df_Mask.pkl")
#
# print(a)
# print(b)
    #
    # for user in listUsers:
    #     r= df.loc[user]
    #     min_max_scaler = preprocessing.MinMaxScaler()
    #     x_scaled = min_max_scaler.fit_transform(r.values.reshape(-1, 1))
    #     print(x_scaled)
        # df_normalized = pd.DataFrame(x_scaled.transpose)
        # df[user]= df_normalized

        #df.loc[user] = x_scaled.shape(10)


        # print(x_scaled)

        # print(df_normalized)
        # print()
        #print(df_normalized.loc[1:])


        #df.loc[user] = [5,5,5,5,5,5,5,5,5,5]

    #print(df)

 # df = DataFrame(results)
 #        usersNumber= len(set(df.ix[0:numRows-1,0]))
 #        listUsers= list(set(df.ix[0:numRows-1,0]))   # WARNING !!!! THE SET OF USERS IS NOT ORDERED
 #        listPOI = df.ix[0:9, 1].tolist()