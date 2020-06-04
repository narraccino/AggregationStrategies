import mysql.connector


def deletetables():

    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                      host='127.0.0.1',
                                      database='poi_dataset')
    cursor = db.cursor()

    try:
           # Execute the SQL command
           #cursor.execute(sql)

            # cursor.execute("DELETE FROM poi")
            # db.commit()
            #
            # cursor.execute("DELETE FROM category")
            # db.commit()

            cursor.execute("DELETE FROM occurrences")
            db.commit()

            print("DELETED ALL TABLES! ")
            # disconnect from server
            db.close()

    except:
            # Rollback in case there is any error
            print("Transaction refused")
            db.close()

