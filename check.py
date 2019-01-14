import mysql.connector

#checking of color

def checkGroups(userID):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    print("UserID: ", +userID)

    try:

        sql = "SELECT q1.namegroup, q1.total, q1.total - q2.sumVoted AS remaining , q1.group_ID " \
              "FROM " \
              "(SELECT namegroup, COUNT(*) AS total, group_ID FROM groupusers RIGHT OUTER JOIN user ON user_ID = %s WHERE namegroup IS NOT NULL GROUP BY namegroup ) q1 " \
              "JOIN " \
              "(SELECT namegroup, SUM(voted) AS sumVoted FROM groupusers RIGHT OUTER JOIN user ON user_ID = %s WHERE voted IS NOT NULL GROUP BY namegroup) q2 " \
              "on q1.namegroup = q2.namegroup"

        cursor.execute(sql, (userID, userID))
        results = cursor.fetchall()
        numRows = len(results)

        if(numRows>0):
            for i in range(numRows):


                nameGroup = results[i][0]
                numTotal = results[i][1]
                numRemaining = results[i][2]
                groupID = results[i][3]

                query = "SELECT `voted` FROM `groupusers` WHERE `ID_user`=%s AND `group_ID`=%s "
                cursor.execute(query, (userID, groupID))
                vote = cursor.fetchone()
                vote= int(vote[0])
                # print(int(vote[0]))

                print("\n\nGroupname: " + nameGroup)
                print("Total members: " + str(numTotal))
                print("Remaining users: " + str(numRemaining))
                if (vote == 1 and numRemaining != 0):
                    print("RED!")
                if (vote == 0 and numRemaining != 0):
                    print("YELLOW!")
                if (vote == 1 and numRemaining == 0):
                    print("GREEN!")
        else:
            print("NO GROUPS FOR YOU")

        db.close()
    except:

        print("Error: unable to fecth data from CHECK")
        db.close()