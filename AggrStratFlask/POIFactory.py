import mysql.connector, flask, json,os, traceback
from SPARQLWrapper import SPARQLWrapper, JSON

def createPOIUser():

    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')


    cursor = db.cursor()


    array = list()
    listPOI = list()
    listCat = list()
    listID = list()
    listSito = list()
    listDescriptions = list()
    d= dict()


    try:

        cursor.execute("SELECT qa.ID_POI, qa.name_POI, qa.link, name_category "
                       "FROM "
                       "(SELECT q1.ID_poi, name_POI, link, ID_category FROM (SELECT * FROM `poi` ORDER BY RAND() LIMIT 10) q1 JOIN `occurrences` ON occurrences.ID_POI = q1.ID_POI) qa "
                       "JOIN `category` ON category.ID_category = qa.ID_category")
        result= cursor.fetchall()

        for row in result:
            id = row[0]
            poi = row[1]
            link = row[2]
            cat = row[3]


            if (poi not in listPOI):
                listID.append(id)
                listPOI.append(poi)
                listSito.append(link)

            if (poi not in d):
                d[poi]= list()
                d[poi].append(cat)
            else:
                d[poi].append(cat)


    except:
        traceback.print_exc()

    db.close()


    for key, value in d.items():
        listCat.append(value)

    for item in listSito:
        listDescriptions.append(getSPARQLDescription(item))

    data = {}
    data['infoPOI'] = []

    for i in range(len(listPOI)):

        data['infoPOI'].append({'poi': listPOI[i], 'cat': ', '.join(str(e) for e in listCat[i]), 'id': listID[i], 'description': listDescriptions[i], 'sito': listSito[i]})

    with open('infoPOI.json', 'w') as file:
        json.dump(data, file)

    #dicto = {"dict": array}
    #return dicto

    return data

def getSPARQLDescription(resourcePOI):

    pois = list()

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")


    try:

        sparql.setQuery("""
            PREFIX dbo: <http://dbpedia.org/ontology/>

            SELECT ?o WHERE { <""" + resourcePOI + """> dbo:abstract ?o . 
            FILTER langMatches(lang(?o), "en")
            } LIMIT 1
        """)


        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()


        description= results["results"]["bindings"][0]["o"]["value"]


    except:
        traceback.print_exc()

    return description

# def createPOIGroup():
#     db = mysql.connector.connect(user='mattarella', password='mattarella',
#                                  host='127.0.0.1',
#                                  database='dbaggregationstrategies')
#
#     cursor = db.cursor()
#
#     listID = list()
#     listPOI = list()
#
#     data = {}
#     data['infoPOI'] = []
#
#     try:
#
#         cursor.execute("SELECT * FROM `poi` ORDER BY RAND() LIMIT 10")
#         result = cursor.fetchall()
#
#         for row in result:
#             id = row[0]
#             poi = row[1]
#             link = row[2]
#
#             listID.append(id) #DA SALVARE !!!!
#             listPOI.append(poi)
#
#             data['infoPOI'].append({'id': id,'poi': poi, 'sito': link})
#
#     except:
#         traceback.print_exc()
#
#     db.close()
#
#
#     with open('infoPOIGroup.json', 'w') as file:
#         json.dump(data, file)
#
#     # dicto = {"dict": array}
#     # return dicto
#
#     return data

def getPOIGroup(groupID, userID):
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    cursor = db.cursor()

    listID = list()
    listPOI = list()
    listCAT= list()
    listDescription = list()
    listLink = list()



    try:

        query= "SELECT q2.ID_POI, q2.name_POI, q2.link " \
                  "FROM (SELECT POI_ID FROM ratings WHERE group_ID = %s AND userID = %s) q1 JOIN poi AS q2 ON q1.POI_ID = q2.ID_POI"

        cursor.execute(query, (groupID, userID))
        result = cursor.fetchall()

        for row in result:
            id = row[0]
            poi = row[1]
            link = row[2]

            listID.append(id)
            listPOI.append(poi)
            listLink.append(link)
            description=getSPARQLDescription(link)
            listDescription.append(description)


        for poi_id in listID:

            query = "SELECT q2.name_category FROM (SELECT * FROM occurrences WHERE ID_POI = %s ) q1 JOIN category AS q2 ON q1.ID_category = q2.ID_category"


            cursor.execute(query, (poi_id,))
            result = cursor.fetchall()
            listRes = list()
            for row in result:
                cat = row[0]
                listRes.append(cat)

            listCAT.append(listRes)

        data = {}
        data['infoPOI'] = []
        for i in range(0,len(listID)):

            data['infoPOI'].append({'id': listID[i], 'poi': listPOI[i], 'cat': listCAT[i], 'description':listDescription[i], 'sito': listLink[i]})

    except:
        traceback.print_exc()

    db.close()
    #
    # with open('infoPOIGroup.json', 'w') as file:
    #     json.dump(data, file)

    # dicto = {"dict": array}
    # return dicto

    return data