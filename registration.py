import mysql.connector, flask, json,os, traceback
from flask import g, session
from clean import deletetables
from random import randint
from check import checkGroups, checkCompleted
from recommendation import recommendation, viewList


#svuoto le tabelle
deletetables()

app = flask.Flask(__name__)
app.secret_key= os.urandom(24)

#Visualize the page index.html with 2 buttons
@app.route("/")
def welcome():
    session['userID']=0
    return flask.render_template("index.html", identification=session['userID'])

#Visualize the page signin.html where a user fills form for registration
@app.route("/signinClick")
def signinClick():
    return flask.render_template("signin.html")

#Visualize the page login.html where the use does a login and puts username and password
@app.route("/createGroupClick")
def createGroupClick():
    return flask.render_template("login.html")

#This method makes a query into the DB and records the informations about the user
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

        username = data["username"]
        password = data["password"]
        try:
           # Execute the SQL command
           #cursor.execute(sql)

           cursor.execute("INSERT INTO user(username, password) VALUES (%s, %s)", (username, password))
           # Commit your changes in the database
           db.commit()
           print("User registered! ")
           # disconnect from server



           sql = """SELECT * FROM user WHERE username = '%s' AND password= '%s'""" % (username, password)

           try:
               cursor.execute(sql)
               results = cursor.fetchall()

               for row in results:
                   session.pop('userID', None)
                   userID = row[0]
                   session['userID'] = userID
           except:
               traceback.print_exc()

           db.close()

           array = list()
           listPOI = list()
           listCat = list()
           listID = list()
           listImages = list()
           listDescriptions = list()
           listSites = list()

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


           return flask.render_template("initRatings.html",  data=dicto)

        except:
            # Rollback in case there is any error
            print("Transaction refused")
            db.close()
            return flask.render_template('error.html')

#Method usd to check if the informations given by a user are into the DB
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

        sql = """SELECT * FROM user WHERE username = '%s' AND password= '%s'""" % (username, password)

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:

                session.pop('userID',None)
                userID = row[0]
                # passw = row[2]
                session['userID']=userID
                # if (passw == password):
                #     # Now print fetched result
                #     print("\nLogged: ", userID, name, passw)
                #     db.close()
                #     listUserID.append(userID)
                #     listUsers.append(username)
                    # return userID,name
                # else:
                #     print("Error username or password")
                #     db.close()

                jsonData = checkGroups(userID)
        except:
            print("Error: unable to fecth data")
            print("Error username or password")
            db.close()

    return flask.render_template("homeUser.html", jsonData=json.dumps(jsonData), userID= session['userID'])

@app.route("/logout")
def logout():
    session.pop('userID', None)
    return flask.render_template("index.html")

@app.route("/homeuser", methods=["GET"])
def homeuser():
    return flask.render_template("nameGroup.html")

#The user gives the name of the group and the number of the members
@app.route("/openAddUser", methods=["POST"])
def openAddUser():
    if flask.request.method == "POST":
        data = flask.request.form

        session['groupName'] = data["groupName"]
        numberOfMembers = data["membersNumber"]


        return flask.render_template("usersgroup.html", data=numberOfMembers, identification= session['userID'])

#The first user gives ratings for the list and then the web app returns the HOME USER page
@app.route("/addRates", methods=["POST"])
def addRates():

    if flask.request.method == "POST":

        data = flask.request.form
        data = data.to_dict(flat=False)
        dicto = json.loads(list(data.keys())[0])
        array = dicto["dict"]
        ratingsArray = [int(e['rating']) for e in array]
        #ratingsArraylists.append(ratingsArray)



        listPOI = list()
        listID = list()


        with open("poi") as file:
            listPOI = file.read().splitlines()
        with open("id") as file:
            listID = file.read().splitlines()


        commitPOI(listID, listPOI)



        groupID= findGroupID(session['userID'], session['groupName'])
        session['groupID']= groupID
        commitRate(groupID, session['userID'], listID, ratingsArray)

        #check if there are groups into DB
        jsonData =checkGroups(session['userID'])

        # userID=session['userID']

        return flask.render_template("homeUser.html", userID=session['userID'], jsonData=json.dumps(jsonData))

@app.route("/addInitRates", methods=["POST"])
def addInitRates():

    if flask.request.method == "POST":

        data = flask.request.form
        data = data.to_dict(flat=False)
        dicto = json.loads(list(data.keys())[0])
        array = dicto["dict"]
        ratingsArray = [int(e['rating']) for e in array]
        #ratingsArraylists.append(ratingsArray)


        listPOI= list()
        listID= list()


        with open("poi") as file:
            listPOI = file.read().splitlines()
        with open("id") as file:
            listID = file.read().splitlines()

        commitPOI(listID, listPOI)

        commitInitRate(session['userID'],listID, ratingsArray)

        jsonData =checkGroups(session['userID'])

        # userID=session['userID']

        return flask.render_template("homeUser.html", userID=session['userID'], jsonData=json.dumps(jsonData))

@app.route("/search", methods=["POST"])
def search():


    countUsers=0


    if flask.request.method == "POST":
        data = flask.request.form

        listUserID= list()
        listUserID.append(session['userID'])

        #data = flask.request.args
        # data = data.to_dict(flat=False)
        print(data)


        data = list(data.values())
        data.remove('default')

        for i in range(0, len(data)):

            userN = data[i]

            db = mysql.connector.connect(user='mattarella', password='mattarella',
                                         host='127.0.0.1',
                                         database='dbaggregationstrategies')

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            #i need to verify if the user exists
            sql ="""SELECT * FROM user WHERE username = '%s'""" % (userN)

            try:

                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    userI = row[0]

                listUserID.append(userI)

                countUsers= countUsers+1

            except:
                print("Error: unable to fetch data")
                listUserID.clear()
                #listUsers.clear()
                db.close()

            db.close()

        # commit e registro gli utenti con voted 0
        commitGroup(listUserID, session['groupName'])

        jsonData = checkGroups(session['userID'])



    return flask.render_template("homeUser.html", jsonData=json.dumps(jsonData), userID=session['userID'])

@app.route("/rates", methods=["GET"])
def rates():
        data = flask.request.args
        data = data.to_dict(flat=False)
        session['groupName']=data['share'][0]
        session['color']= data['color'][0]

        if (session['color'] == 'red'):
            jsonData = checkGroups(session['userID'])

            return flask.render_template("homeUser.html", jsonData=json.dumps(jsonData), userID=session['userID'])

        if(session['color']== 'yellow'):
            array = list()
            listPOI = list()
            listCat = list()
            listID = list()
            listImages = list()
            listDescriptions = list()
            listSites = list()

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

            return flask.render_template("ratings.html", data=dicto)

        if(session['color']== 'green'):

            groupID = findGroupID(session['userID'], session['groupName'])
            fa_state, less_state = checkCompleted(groupID)

            if(not fa_state and not less_state):
                lmw, fa = viewList(groupID)
                return flask.render_template("recommendation.html", lmw=lmw, fa=fa)
            else:
                recommendation(groupID)
                lmw, fa = viewList(groupID)
                return flask.render_template("recommendation.html", lmw=lmw, fa=fa)

#commit of groupname and userID of that group
def commitGroup(listUserID, groupName):
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

            cursor.execute("INSERT INTO groupusers(group_ID, ID_user, namegroup, voted) VALUES (%s, %s, %s, %s)", (groupID,listUserID[i], groupName, 0))
            # Commit your changes in the database
            db.commit()


            print("Group registered! ")
        except:
            # Rollback in case there is any error
            db.rollback()
            print("Transaction group refused")

    cursor.execute("INSERT INTO stategroupalgorithm(group_ID, algorithm_ID, completed) VALUES (%s, %s, %s)", (groupID, 1, 0))
    db.commit()
    cursor.execute("INSERT INTO stategroupalgorithm(group_ID, algorithm_ID, completed) VALUES (%s, %s, %s)", (groupID, 2, 0))
    db.commit()

    db.close()

#commit of list ID and listPOI
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

#commit of ID groupID, listID, listIDPOI and ratings
def commitRate(groupID,userID, listIDPOI, ratingsArray):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    #for i in range(0, len(listID)):
    for j in range(0, len(listIDPOI)):
        try:
            # Execute the SQL command
            # cursor.execute(sql)

            cursor.execute("INSERT INTO ratings(group_ID,userID, POI_ID,rate) VALUES (%s, %s, %s, %s)",(groupID, userID, listIDPOI[j], ratingsArray[j]))

            # Commit your changes in the database
            db.commit()
            print("POI registered! ")
        except Exception:
            traceback.print_exc()
            db.rollback()
            print("Transaction POI refused2")




    try:
        sql = "UPDATE groupusers SET voted=%s WHERE group_ID=%s AND ID_user=%s"
        cursor.execute(sql, (1,groupID, userID))

        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        print("Transaction voted refused")


    db.close()

def findGroupID(userID, groupName):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        # Execute the SQL command
        # cursor.execute(sql)

        query = "SELECT group_ID FROM groupusers WHERE ID_user=%s AND namegroup=%s"
        cursor.execute(query, (userID, groupName))

        results = cursor.fetchall()
        group= results[0]
        groupID = group[0]
        #print(groupID[0])
        print("group ID founded")

    except:
        # Rollback in case there is any error

        print("group id not founded")

    # disconnect from server
    db.close()
    return groupID

def commitInitRate(userID, listIDPOI, ratingsArray):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    #for i in range(0, len(listID)):
    for j in range(0, len(listIDPOI)):
        try:
            # Execute the SQL command
            # cursor.execute(sql)

            cursor.execute("INSERT INTO init_ratings(ID_user, POI_ID,rating) VALUES (%s, %s, %s)",(userID, listIDPOI[j], ratingsArray[j]))

            # Commit your changes in the database
            db.commit()
            print("Initial rating submitted ")
        except Exception:
            traceback.print_exc()
            db.rollback()
            print("Transaction rating FAILED")




    # try:
    #     sql = "UPDATE groupusers SET voted=%s WHERE group_ID=%s AND ID_user=%s"
    #     cursor.execute(sql, (1,groupID, userID))
    #
    #     # Commit your changes in the database
    #     db.commit()
    # except:
    #     # Rollback in case there is any error
    #     db.rollback()
    #     print("Transaction voted refused")


    db.close()

if __name__ == "__main__":
    print("SEMAUTO Group Recommender System")



    app.run()
