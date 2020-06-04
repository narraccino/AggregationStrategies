from SPARQLWrapper import SPARQLWrapper, JSON
import json

with open("POItrovati.txt") as file:
    listPOI = file.read().splitlines()


def getSPARQLDescription(resourcePOI):

    pois = set()

    try:

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")

        for type in resourcePOI:
            sparql.setQuery(""" 
            
                    PREFIX   dct: <http://purl.org/dc/terms/>

                    SELECT ?cat WHERE {

                       <""" + type + """> dct:subject ?cat .

                    }

                    """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            for result in results["results"]["bindings"]:
                pois.add(result["cat"]["value"])
            #     print(result["cat"]["value"])
            # print('\n')


    except:
        pass

    return pois

pois = getSPARQLDescription(listPOI)

file= open("CATtrovati", "w", encoding="utf-32")

for poi in pois:
    print(poi)
    file.write(poi)
    file.write('\n')

file.close()








# for poi in pois:
#     print(poi)

# des= getSPARQLDescription("ARTIS")
# print(des)


#
#
# """
#
# PREFIX schema: <http://schema.org/>
# PREFIX wikibase: <http://wikiba.se/ontology#>
# PREFIX wd: <http://www.wikidata.org/entity/>
# PREFIX wdt: <http://www.wikidata.org/prop/direct/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#
# SELECT ?id ?article WHERE {
#
#     ?id rdfs:label ?label .
#
#     ?id wdt:P31 ?type .
#     ?type rdfs:label "zoo"@en .
#
#     ?id wdt:P17 ?country .
#     ?country rdfs:label "Netherlands"@en .
#
#     ?article schema:about ?id .
#     ?article schema:inLanguage "en" .
#
#     FILTER (lcase(str(?label)) = "artis")
#     FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
# }
#
# LIMIT 1
#
# """

