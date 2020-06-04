from SPARQLWrapper import SPARQLWrapper, JSON
import json

with open("poi.txt") as file:
    listPOI = file.read().splitlines()


def getSPARQLDescription(listTypes):
    file = open("POItrovati.txt", "w")
    pois = set()
    try:

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")

        for type in listTypes:
            sparql.setQuery(""" 

                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX yago: <http://dbpedia.org/class/yago/>

                    SELECT ?poi WHERE {

                       ?poi rdf:type """ + type + """ .

                    }

                    """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            for result in results["results"]["bindings"]:
                # pois.add(result["poi"]["value"])
                file.write(result["poi"]["value"]+'\n')

        file.close()
    #
    except:
        pass




getSPARQLDescription(listPOI)


# for poi in pois:
#     print(poi)
#     file.write(poi)

# file.close()












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

