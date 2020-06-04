import mysql.connector
import traceback





db = mysql.connector.connect(user='mattarella', password='mattarella',
                             host='127.0.0.1',
                             database='dbaggregationstrategies')


# prepare a cursor object using cursor() method
cursor = db.cursor()


try:
    groupID = 2325261
    # sql = "SELECT userID, POI_ID, rate FROM ratings WHERE group_ID=%s "
    #
    #
    # cursor.execute(sql, groupID)

    cursor.execute(" SELECT userID , POI_ID , rate FROM ratings WHERE group_ID = %s ", (groupID,))
    results = cursor.fetchall()
    numRows = len(results)
    # print(results)

    for i in range(numRows):
        ID_user = results[i][0]
        ID_POI = results[i][1]
        rate = results[i][2]



    db.close()

except:
    traceback.print_exc()
    db.close()