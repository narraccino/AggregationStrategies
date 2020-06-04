import mysql.connector
import traceback
from tqdm import tqdm


db = mysql.connector.connect(user='mattarella', password='mattarella',
                             host='127.0.0.1',
                             database='mini_poi_dataset')

cursor = db.cursor()

#POI sospetti (se hanno una sola riga)
try:
    cursor.execute("SELECT * FROM occurrences GROUP BY ID_POI HAVING COUNT(*) = 1 ")
    result = cursor.fetchall()

except:
    traceback.print_exc()


pbar = tqdm(total=len(result))

for row in result:
    try:
        ID_POI= row[0]
        ID_category = row[1]
        cursor.execute("SELECT * FROM occurrences WHERE ID_category= %s ", (ID_category,))
        numRows = len(cursor.fetchall())
        if (numRows<=1):
            cursor.execute("DELETE FROM category WHERE ID_category = %s ", (ID_category,))
            db.commit()
            cursor.execute("DELETE FROM poi WHERE ID_POI= %s ", (ID_POI,))
            db.commit()
            cursor.execute("DELETE FROM occurrences WHERE ID_POI= %s AND ID_category= %s ", (ID_POI,ID_category))
            db.commit()
    except:
        traceback.print_exc()

    pbar.update(1)

db.close()
pbar.close()