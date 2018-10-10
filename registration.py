import mysql.connector, flask, json
from random import randint
from FA import FairenessAverage
from LMW import LeastMostWithout
import numpy as np

listUserID = list()
listUsers = list()
ratingsArraylists = list()
groupName = ""
listPOI = list()
listCat = list()
listID = list()
listImages = list()
listDescriptions = list()
listSites = list()

check = False
index = 0


app = flask.Flask(__name__)

@app.route("/")
def welcome():
    return flask.render_template("index.html")

@app.route("/signinClick")
def signinClick():
    return flask.render_template("signin.html")

@app.route("/createGroupClick")
def createGroupClick():
    return flask.render_template("login.html")

@app.route("/signin", methods=["POST"])
def signin():
    if flask.request.method == "POST":
        data = flask.request.form

        db = mysql.connector.connect(user='mattarella', password='mattarella',
                                      host='127.0.0.1',
                                      database='dbaggregationstrategies')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.


        #sql = "INSERT INTO user(username, password) VALUES ('"+username+"', '"+password+"')"

        username = data["name"]
        password = data["password"]
        try:
           # Execute the SQL command
           #cursor.execute(sql)

           cursor.execute("INSERT INTO user(username, password) VALUES (%s, %s)", (username, password))
           # Commit your changes in the database
           db.commit()
           print("User registered! ")
           # disconnect from server
           db.close()
           return flask.render_template("index.html")

        except:
            # Rollback in case there is any error
            print("Transaction refused")
            db.close()
            return flask.render_template('error.html')


@app.route("/login", methods=["POST"])
def login():
    if flask.request.method == "POST":
        data = flask.request.form

        db = mysql.connector.connect(user='mattarella', password='mattarella',
                                     host='127.0.0.1',
                                     database='dbaggregationstrategies')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        username = data["name"]
        password = data["password"]

        sql = """SELECT * FROM user WHERE username = '%s'""" % (username)

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                userID = row[0]
                name = row[1]
                passw = row[2]

                if (passw == password):
                    # Now print fetched result
                    print("\nLogged: ", userID, name, passw)
                    db.close()
                    listUserID.append(userID)
                    listUsers.append(username)
                    return flask.render_template("namegroup.html")
                    # return userID,name
                else:
                    print("Error username or password")
                    db.close()

        except:
            print("Error: unable to fecth data")
            db.close()


@app.route("/openAddUser", methods=["POST"])
def openAddUser():
    if flask.request.method == "POST":
        data = flask.request.form
        groupName = data["groupName"]
        numberOfMembers = data["membersNumber"]

        return flask.render_template("usersgroup.html", data=numberOfMembers)


@app.route("/addRates", methods=["POST"])
def addRates():

    if flask.request.method == "POST":

        data = flask.request.form
        data = data.to_dict(flat=False)
        dicto = json.loads(list(data.keys())[0])
        array = dicto["dict"]
        ratingsArray = [int(e['rating']) for e in array]
        ratingsArraylists.append(ratingsArray)

        global index

        index += 1

        print(index, listUsers)

        if not(index == (len(listUserID))):

            return flask.render_template("otherUsersLogin.html", user=listUsers[index])

        else:

            # we convert the ratingsArrayLists in array
            ratingsArrayPOI = np.array(ratingsArraylists)
            print(ratingsArrayPOI)

            # fairenessAverage algorithm
            final_listA = FairenessAverage(ratingsArrayPOI, listPOI, listUsers)
            print("The ordered list with FairenessAverage is this:")
            for i in range(0, len(listPOI)):
                print(i + 1, '.', final_listA[i])

            print('\n\n')

            # LeastMostWithout algorithm
            final_listB, len_POIModified = LeastMostWithout(ratingsArrayPOI, listPOI, listUsers)
            print("The ordered list with LeastMostWithout is this:")
            for i in range(0, len_POIModified):
                print(i + 1, '.', final_listB[i])

            groupID = commitGroup(listUserID, groupName)
            commitPOI(listID, listPOI)
            commitRate(groupID, listUserID, listID, ratingsArrayPOI)
            index = 0

            fairness_dict = {"fairness": final_listA}

            least_dict = {"least": final_listB}

            return flask.render_template("recommendation.html", fairness=fairness_dict, least=least_dict)


@app.route("/search", methods=["POST"])
def search():

    global check

    if flask.request.method == "POST":
        data = flask.request.form
        user_already_logged = listUserID[0]

        if not(check):

            data = list(data.values())

            data.remove('default')

            for i in range(0, len(data)):

                userN = data[i]

                print(userN)

                db = mysql.connector.connect(user='mattarella', password='mattarella',
                                             host='127.0.0.1',
                                             database='dbaggregationstrategies')

                # prepare a cursor object using cursor() method
                cursor = db.cursor()

                sql ="""SELECT * FROM user WHERE username = '%s'""" % (userN)
                # sql = """SELECT * FROM user"""
                try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    # Fetch all the rows in a list of lists.
                    results = cursor.fetchall()
                    for row in results:
                        userID = row[0]
                        name = row[1]

                    listUserID.append(userID)
                    listUsers.append(name)

                except:
                    print("Error: unable to fetch data")
                    db.close()

            db.close()

            check = True

        # check in db
        if index > 0:

            db = mysql.connector.connect(user='mattarella', password='mattarella',
                                         host='127.0.0.1',
                                         database='dbaggregationstrategies')

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            username = data["name"]
            password = data["password"]

            sql = """SELECT * FROM user WHERE username = '%s'""" % (username)

            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                for row in results:
                    userID = row[0]
                    name = row[1]
                    passw = row[2]

                    if not(passw == password):
                        print("Error username or password")
                        db.close()

            except:
                print("Error: unable to fecth data")
                db.close()

        array = list()

        for i in range(len(listPOI)):
            d = dict()
            d['poi'] = listPOI[i]
            d['cat'] = listCat[i]
            d['id'] = listID[i]
            d['image'] = listImages[i]
            d['description'] = listDescriptions[i]
            d['sito'] = listSites[i]

            array.append(d)

        dicto = {"dict": array}

        # user that created the group
        # return flask.render_template("ratings.html") # todo passare list poi e list cat

        return flask.render_template("ratings.html", data=dicto)


def commitGroup(listUserID, nameGroup):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                  host='127.0.0.1',
                                  database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    groupID= randint(0, 10000000)

    for i in range(0, len(listUserID)):

        try:
            # Execute the SQL command
            #cursor.execute(sql)

            cursor.execute("INSERT INTO groupusers(group_ID, ID_user, namegroup) VALUES (%s, %s, %s)", (groupID,listUserID[i], nameGroup))

            # Commit your changes in the database
            db.commit()

            print("Group registered! ")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("Transaction group refused")




    # disconnect from server
    db.close()

    # print("%d. %s appears %d times." % (i, key, wordBank[key]))

    return groupID


def commitPOI(listIDPOI,listPOI):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                  host='127.0.0.1',
                                  database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    for i in range(0, len(listIDPOI)):

        try:
           # Execute the SQL command
           #cursor.execute(sql)

           cursor.execute("INSERT INTO poi(POI_ID, name_POI) VALUES (%s, %s)", (listIDPOI[i], listPOI[i]))

           # Commit your changes in the database
           db.commit()
           print("POI registered! ")
        except:
           # Rollback in case there is any error
           db.rollback()
           print("Transaction POI refused")




    # disconnect from server
    db.close()

    # print("%d. %s appears %d times." % (i, key, wordBank[key]))

    return


def commitRate(groupID, listID, listIDPOI, ratingsArrayPOI):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    for i in range(0, len(listID)):
        for j in range(0, len(listIDPOI)):
            try:
                # Execute the SQL command
                # cursor.execute(sql)

                cursor.execute("INSERT INTO ratings(group_ID,userID, POI_ID,rate) VALUES (%s, %s, %s, %s)",(groupID, listID[i], listIDPOI[j], int(ratingsArrayPOI[i][j])))
                #cursor.execute("INSERT INTO ratings(group_ID,userID, POI_ID,rate) VALUES (%s, %s, %s, %s)",(4843874, 21, '4a2705d8f964a52012891fe3', 5))

                # Commit your changes in the database
                db.commit()
                print("POI registered! ")
            except:
                # Rollback in case there is any error
                db.rollback()
                print("Transaction POI refused2")

            # disconnect from server
    db.close()

    # print("%d. %s appears %d times." % (i, key, wordBank[key]))

    return


if __name__ == "__main__":
    print("Loading Group Recommender System")

    # [listPOI, listCat, listID, listImages] = topResults()
    #
    #
    # file = open("poi", 'w')
    # file.write('\n'.join(listPOI))
    # file.close()
    #
    # file = open("cat", 'w')
    # file.write('\n'.join(listCat))
    # file.close()
    #
    # file = open("id", 'w')
    # file.write('\n'.join(listID))
    # file.close()
    #
    # file = open("imgs", 'w')
    # file.write('\n'.join(listImages))
    # file.close()

    with open("poi") as file:
        listPOI = file.read().splitlines()
    with open("cat") as file:
        listCat = file.read().splitlines()
    with open("id") as file:
        listID = file.read().splitlines()
    with open("imgs") as file:
        listImages = file.read().splitlines()
    with open("descriptions") as file:
        listDescriptions = file.read().splitlines()
    with open("site") as file:
        listSites = file.read().splitlines()


    app.run()
