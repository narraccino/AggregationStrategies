import mysql.connector
import pandas as pd
import traceback
import pickle
import numpy as np
from tqdm import tqdm
from tempfile import TemporaryFile

db = mysql.connector.connect(user='mattarella', password='mattarella',
                             host='127.0.0.1',
                             database='poi_dataset')

# prepare a cursor object using cursor() method
cursor = db.cursor()

listaIDPOI= list()
listaIDCAT = list()


try:
    sql = """SELECT ID_POI FROM poi WHERE 1"""
    cursor.execute(sql)
    results = cursor.fetchall()
    pbar1 = tqdm(total=len(results))
    for row in results:
        listaIDPOI.append(row[0])
        pbar1.update(1)

    pbar1.close()
    print('\n\n')

    sql = """SELECT ID_category FROM category WHERE 1"""
    cursor.execute(sql)
    results = cursor.fetchall()
    pbar2 = tqdm(total=len(results))
    for row in results:
        listaIDCAT.append(row[0])
        pbar2.update(1)

    pbar2.close()



    mask = np.zeros((len(listaIDPOI), len(listaIDCAT)), dtype=np.int8)



    sql = """SELECT * FROM occurrences WHERE 1"""
    cursor.execute(sql)
    results = cursor.fetchall()
    pbar3 = tqdm(total=len(results))
    for row in results:
        mask[listaIDPOI.index(row[0])][listaIDCAT.index(row[1])] = 1
        pbar3.update(1)

    pbar3.close()

    db.close()
    # df_Mask_Empty = pd.DataFrame(index=listaIDPOI, columns=listaIDCAT,data=0).astype(np.float32)
    # df_Mask_Empty.to_pickle("./df_Mask.pkl")
    # print(df_Mask_Empty)

    with open('listaIDPOI.pkl', 'wb') as f1:
        pickle.dump(listaIDPOI, f1)
    f1.close()

    with open('listaIDCAT.pkl', 'wb') as f2:
        pickle.dump(listaIDCAT, f2)
    f2.close()


    np.save('mask.npy', mask)



    # with open('listaIDPOI.pkl', 'rb') as f1:
    #     l1 = pickle.load(f1)
    #
    # with open('listaIDCAT.pkl', 'rb') as f2:
    #     l2 = pickle.load(f2)







    #print(df_Mask)


except:
    traceback.print_exc()


