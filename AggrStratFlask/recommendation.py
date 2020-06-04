import mysql.connector
import traceback
from pandas import DataFrame
import numpy as np
from FA import FairenessAverage
from LMW import LeastMostWithout




def recommendation(groupID):

    ratingsArrayPOI = list()



    # ratingsArray = [int(e['rating']) for e in array]

    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')


    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    try:



        cursor.execute(" SELECT userID , POI_ID , rate FROM ratings WHERE group_ID = %s ORDER BY userID", (groupID,))
        results = cursor.fetchall()
        numRows = len(results)

        # db.close()


        df = DataFrame(results)
        usersNumber= len(set(df.ix[0:numRows-1,0]))
        listUsers= list(set(df.ix[0:numRows-1,0]))
        listPOI = df.ix[0:9, 1].tolist()

        #print(df)
        #print(df.ix[0:10,2].tolist())

        j=0
        for i in range(0,usersNumber):
            userratings= df.ix[j:j+9, 2].tolist()
            ratingsArrayPOI.append(userratings)
            j += 10


#FAIRENESS AVERAGE


        # fairenessAverage algorithm
        final_listA = FairenessAverage(ratingsArrayPOI, listPOI, listUsers)

        for i in range(0, len(listPOI)):
            # print(i + 1, '.', final_listA[i])
            cursor.execute("INSERT INTO results(group_ID, POI_ID, algorithm_ID, location ) VALUES (%s, %s, %s, %s)", (groupID, final_listA[i], 1, i+1))
            # Commit your changes in the database
            db.commit()

        sql = "UPDATE stategroupalgorithm SET completed=%s WHERE group_ID=%s AND algorithm_ID=%s"
        cursor.execute(sql, (1, groupID, 1))
        db.commit()

# LeastMostWithout algorithm
        final_listB, len_POIModified = LeastMostWithout(ratingsArrayPOI, listPOI, listUsers)

        for i in range(0, len_POIModified):
            #print(i + 1, '.', final_listB[i])
            cursor.execute("INSERT INTO results(group_ID, POI_ID, algorithm_ID, location ) VALUES (%s, %s, %s, %s)", (groupID, final_listB[i], 2, i + 1))
            # Commit your changes in the database
            db.commit()

        sql = "UPDATE stategroupalgorithm SET completed=%s WHERE group_ID=%s AND algorithm_ID=%s"
        cursor.execute(sql, (1, groupID, 2))
        db.commit()




        db.close()

    except:
        traceback.print_exc()
        db.close()






def viewList (groupID):

    faList = list()
    lmwList = list()

    try:
        db = mysql.connector.connect(user='mattarella', password='mattarella',
                                     host='127.0.0.1',
                                     database='dbaggregationstrategies')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # FINAL LISTS ORDERED

        # print("The ordered list with LeastMostWithout is this:")
        cursor.execute("SELECT name_POI FROM results JOIN poi ON results.POI_ID = poi.ID_POI WHERE algorithm_ID=1 AND group_ID= %s ORDER BY location ASC ", (groupID,))
        lmw = cursor.fetchall()

        for i in range(0, len(lmw)):
            # print(lmw[i][0])
            lmwList.append(lmw[i][0])

        # print("\n\n\nThe ordered list with FairenessAverage is this:")
        cursor.execute("SELECT name_POI FROM results JOIN poi ON results.POI_ID = poi.ID_POI WHERE algorithm_ID=2 AND group_ID= %s ORDER BY location ASC ", (groupID,))
        fa = cursor.fetchall()

        for i in range(0, len(fa)):
            # print(fa[i][0])
            faList.append(fa[i][0])

    except:
        traceback.print_exc()



    return lmwList, faList