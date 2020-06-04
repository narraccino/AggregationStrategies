import mysql.connector, json, traceback

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

        data = {}
        data['numResults']= numRows
        data['infoGroups'] = []

        # data={}
        # data['rows']= numRows
        # jsonData = json.dumps(numRows)
        obj=""

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
                    state="red"
                if (vote == 0 and numRemaining != 0):
                    print("YELLOW!")
                    state="yellow"
                if (vote == 1 and numRemaining == 0):
                    print("GREEN!")
                    state="green"


                data['infoGroups'].append({'nameGroup': nameGroup, 'nameTotal':str(numTotal), 'numRemaining': str(numRemaining), 'state':str(state)})


        else:
            print("NO GROUPS FOR YOU")

            return data

        db.close()
    except Exception:
        traceback.print_exc()
        nameGroup="NO GROUPS FOR YOU!"
        print("Error: unable to fecth data from CHECK")
        db.close()

    # with open('data.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # print(json.dumps(data))

    return data

def checkCompleted(groupID):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:

        cursor.execute("SELECT completed FROM stategroupalgorithm WHERE group_ID = %s AND algorithm_ID = 1", (groupID,))
        fairness = cursor.fetchone()
        cursor.execute("SELECT completed FROM stategroupalgorithm WHERE group_ID = %s AND algorithm_ID = 2", (groupID,))
        lessMostWithout = cursor.fetchone()
        db.close()
    except:
        traceback.print_exc()
        db.close()

    return bool(fairness[0]), bool(lessMostWithout[0])
