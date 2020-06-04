from SPARQLWrapper import SPARQLWrapper, JSON
import pickle
import codecs
import traceback
from tqdm import tqdm


with codecs.open("POItrovati.txt", 'r' , encoding='utf-8') as file:
    resourcePOI = file.read().splitlines()


categories={}

pbar = tqdm(total=len(resourcePOI))


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

        # print(str(i))
        # i=i+1
        #     print(result["cat"]["value"])
        # print('\n')

        categories[type] = list(cats)

        pbar.update(1)


    except:
        traceback.print_exc()
        continue



pbar.close()
f= open("dict_categories.pickle", "wb")
pickle.dump(categories, f)
f.close()

