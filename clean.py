import mysql.connector


def deletetables():

    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                      host='127.0.0.1',
                                      database='dbaggregationstrategies')
    cursor = db.cursor()

    try:
           # Execute the SQL command
           #cursor.execute(sql)

           cursor.execute("DELETE FROM groupusers")
           cursor.execute("DELETE FROM poi")
           cursor.execute("DELETE FROM ratings")
           cursor.execute("DELETE FROM results")
           # Commit your changes in the database
           db.commit()
           print("DELETED ALL TABLES! ")
           # disconnect from server


    except:
            # Rollback in case there is any error
            print("Transaction refused")
            db.close()

