from clean import deletetables
import mysql.connector
import traceback, pickle
from tqdm import tqdm

# def checkCategory(name_category):
#
#     result=0
#
#     db = mysql.connector.connect(user='mattarella', password='mattarella',
#                                  host='127.0.0.1',
#                                  database='poi_dataset')
#
#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
#     try:
#         cursor.execute("SELECT name_category FROM category WHERE name_category = %s", (name_category,))
#         result = cursor.rowcount
#         db.close()
#     except:
#         traceback.print_exc()
#         db.close()
#
#     return result

# def commitPOICategory(name_POI, name_category):
#     db = mysql.connector.connect(user='mattarella', password='mattarella',
#                                  host='127.0.0.1',
#                                  database='poi_dataset')
#
#     cursor = db.cursor()
#
#     try:
#         # Execute the SQL command
#         # cursor.execute(sql)
#
#         query = "SELECT ID_POI FROM poi WHERE name_POI=%s"
#         cursor.execute(query, (name_POI,))
#         ID_POI = cursor.fetchone()
#
#
#
#         query = "SELECT ID_category FROM category WHERE name_category=%s"
#         cursor.execute(query, (name_category,))
#         ID_category = cursor.fetchone()
#
#         cursor.execute("INSERT INTO occurrences(ID_POI, ID_category) VALUES (%s, %s)", (ID_POI[0], ID_category[0]))
#         db.commit()
#
#
#
#     except:
#         traceback.print_exc()
#         db.close()
#
#
#
#     # disconnect from server
#     db.close()


#deletetables()

a = open("dict_categories.pickle", "rb")
dizionario = pickle.load(a)



# dizionario = {}
# for k, v in diz.items():
#     if k == 'http://dbpedia.org/resource/Belmore_Mountain':
#         dizionario[k] = v


pbar = tqdm(total=len(dizionario))

db = mysql.connector.connect(user='mattarella', password='mattarella',
                             host='127.0.0.1',
                             database='poi_dataset')

cursor = db.cursor(buffered=True)


for link_POI,link_cat_list in dizionario.items():
    pbar.update(1)
    if (len(link_cat_list) > 0):

        try:
            name_POI = link_POI.split("http://dbpedia.org/resource/", )[1].replace("_", " ")
            cursor.execute("INSERT INTO poi(name_POI, link) VALUES (%s, %s)", (name_POI, link_POI))
            db.commit()

            for i in range(0,len(link_cat_list)):
                link_cat = link_cat_list[i]
                name_category = link_cat.split("http://dbpedia.org/resource/Category:", )[1].replace("_", " ")


                try:
                    #result=0
                    cursor.execute("SELECT name_category FROM category WHERE name_category = %s", (name_category,))
                    result = cursor.rowcount

                except:
                    traceback.print_exc()


                if(result==0):
                    cursor.execute("INSERT INTO category(name_category, link) VALUES (%s, %s)", (name_category, link_cat))
                    db.commit()
                    try:

                        query = "SELECT ID_POI FROM poi WHERE name_POI=%s"
                        cursor.execute(query, (name_POI,))
                        ID_POI = cursor.fetchone()

                        query = "SELECT ID_category FROM category WHERE name_category=%s"
                        cursor.execute(query, (name_category,))
                        ID_category = cursor.fetchone()

                        cursor.execute("INSERT INTO occurrences(ID_POI, ID_category) VALUES (%s, %s)", (ID_POI[0], ID_category[0]))
                        db.commit()



                    except:
                        traceback.print_exc()
                        # db.close()


        except:
            traceback.print_exc()



db.close()
pbar.close()