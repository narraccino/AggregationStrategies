from SPARQLWrapper import SPARQLWrapper, JSON
import traceback
from clean import deletetables
import mysql.connector

import traceback
from collections import Counter
import json

def checkCategory(name_category):

    result=0

    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
        cursor.execute("SELECT name_category FROM category WHERE name_category = %s", (name_category,))
        result = cursor.rowcount()
        db.close()
    except:
        db.close()

    return result

def commitPOICategory(name_POI, name_category):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='poi_dataset')

    # prepare a cursor object using cursor() method

    cursor = db.cursor(buffered=True)

    try:
        # Execute the SQL command
        # cursor.execute(sql)

        query = "SELECT ID_POI FROM poi WHERE name_POI=%s"
        cursor.execute(query, (name_POI,))
        ID_POI = cursor.fetchone()



        query = "SELECT ID_category FROM category WHERE name_category=%s"
        cursor.execute(query, (name_category,))
        ID_category = cursor.fetchone()

        cursor.execute("INSERT INTO occurrences(ID_POI, ID_category) VALUES (%s, %s)", (ID_POI[0], ID_category[0]))
        db.commit()



    except:
        # Rollback in case there is any error
        #traceback.print_exc()
        db.close()
        print(str(ID_POI[0]) + " , " + str(ID_category[0]))

    # disconnect from server
    db.close()



file = open("POItrovati.txt", "r", encoding="utf-16")
#with open("POItrovati.txt") as file:
listPOI = file.read().splitlines()



db = mysql.connector.connect(user='mattarella', password='mattarella',
                             host='127.0.0.1',
                             database='poi_dataset')


# prepare a cursor object using cursor() method
cursor = db.cursor()


#deletetables()

for type in listPOI:

    try:

        name_POI = type.split("http://dbpedia.org/resource/",)[1]

        cursor.execute("INSERT INTO poi(name_POI, link) VALUES (%s, %s)", (name_POI, type))
        db.commit()
        # results = cursor.fetchall()
    except:
        continue


    # pois = list()

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")


    try:

        sparql.setQuery(""" 

                    PREFIX   dct: <http://purl.org/dc/terms/>

                    SELECT ?cat WHERE {

                       <""" + type + """> dct:subject ?cat .

                    }

                    """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # cats = set()
        for result in results["results"]["bindings"]:
            cat= result["cat"]["value"]
            name_category = cat.split("http://dbpedia.org/resource/Category:", )[1]
            check= checkCategory(name_category)
            if(check==0):
                cursor.execute("INSERT INTO category(name_category, link) VALUES (%s, %s)", (name_category, cat))
                db.commit()
            commitPOICategory(name_POI, name_category)

        #     print(result["cat"]["value"])
        # print('\n')

        # pois += list(cats)


    except:
        traceback.print_exc()


db.close()


# file = open("CATtrovati_duplicati.txt", "w", encoding="utf-32")
#
# for poi in pois:
#     # print(poi)
#     file.write(poi)
#     file.write('\n')
#
# file.close()
