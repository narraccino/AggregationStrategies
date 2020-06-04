import mysql.connector

db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:

    # query = "SELECT group_ID FROM groupusers WHERE ID_user=%s AND namegroup=%s"
    # cursor.execute(query, (39,"TUDELFT" ))
    #cursor.execute("INSERT INTO ratings(group_ID,userID, POI_ID,rate) VALUES (%s, %s, %s, %s)", (54, 32, 44, int(ratingsArrayPOI[j])))

    sql = "UPDATE groupusers SET voted=%s WHERE group_ID=%s AND ID_user=%s"
    cursor.execute(sql, (1, 559019, 39))

    # results = cursor.fetchall()
    # groupID = results[0]
    # print(groupID[0])
    print("group ID founded")
    db.commit()
except:
    # Rollback in case there is any error

    print("group id not founded")

# disconnect from server
db.close()