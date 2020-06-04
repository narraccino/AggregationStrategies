from clean import deletetables
import mysql.connector
import traceback, pickle
from tqdm import tqdm




a = open("dict_categories.pickle", "rb")
dizionario = pickle.load(a)


deletetables()

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
            query = "SELECT ID_POI FROM poi WHERE name_POI=%s"
            cursor.execute(query, (name_POI,))
            ID_POI = cursor.fetchone()

            for i in range(0,len(link_cat_list)):
                link_cat = link_cat_list[i]
                name_category = link_cat.split("http://dbpedia.org/resource/Category:", )[1].replace("_", " ")

                try:

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