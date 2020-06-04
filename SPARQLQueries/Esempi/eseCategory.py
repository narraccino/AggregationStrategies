from collections import Counter

from SPARQLWrapper import SPARQLWrapper, JSON
import pickle
import codecs
import traceback



with codecs.open("esePOI.txt", 'r' , encoding='utf-8') as file:
    listPOI = file.read().splitlines()


categories={}

def getSPARQLDescription(resourcePOI):
    pois = list()

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    for type in resourcePOI:


        try:

            sparql.setQuery(""" 

                        PREFIX   dct: <http://purl.org/dc/terms/>

                        SELECT ?cat WHERE {

                           <""" + type + """> dct:subject ?cat .

                        }

                        """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            cats = set()
            for result in results["results"]["bindings"]:
                cats.add(result["cat"]["value"])
            #     print(result["cat"]["value"])
            # print('\n')

            categories[type] = list(cats)


        except:
            traceback.print_exc()




getSPARQLDescription(listPOI)


f= open("file.pickle", "wb")
pickle.dump(categories, f)
f.close()
print(categories)
print('\n')

a = open("file.pickle", "rb")
dizionario = pickle.load(a)
print(dizionario)

a.close()


# file = open("CATtrovati_duplicati.txt", "w", encoding="utf-32")
#
# for poi in pois:
#     # print(poi)
#     file.write(poi)
#     file.write('\n')
#
# file.close()

