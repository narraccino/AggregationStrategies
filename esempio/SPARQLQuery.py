from SPARQLWrapper import SPARQLWrapper, JSON
import json


def getSPARQLDescription(poiName, listTypes):

    poiName = poiName.lower()

    for type in listTypes:

        try:
            sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
            country= "Netherlands"
            #type = "Museum"
            sparql.setQuery("""
            
            PREFIX schema: <http://schema.org/>
            PREFIX wikibase: <http://wikiba.se/ontology#>
            PREFIX wd: <http://www.wikidata.org/entity/>
            PREFIX wdt: <http://www.wikidata.org/prop/direct/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    
            SELECT ?id ?article WHERE {
                
                ?id rdfs:label ?label .
              
                ?id wdt:P31 ?type .
                ?type rdfs:label \"""" + type + """\"@en .
              
                ?id wdt:P17 ?country .
                ?country rdfs:label \"""" + country + """\"@en .
                
                ?article schema:about ?id .
                ?article schema:inLanguage "en" .
                
                FILTER (lcase(str(?label)) = \"""" + poiName + """\")
                FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
            } 
            
            LIMIT 1
            
            """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            # description= results["results"]["bindings"][0]["d"]["value"]
            # return description

            #print(results["results"]["bindings"][0]["id"]["value"])
            #print(results["results"]["bindings"][0]["article"]["value"])

            uri = str(results["results"]["bindings"][0]["article"]["value"])
            uri = uri.replace('en.wikipedia', 'dbpedia')
            uri = uri.replace('wiki', 'resource')
            uri = uri.replace('https', 'http')

            #print(uri)

            sparql = SPARQLWrapper("http://dbpedia.org/sparql")
            sparql.setQuery(""" 
    
                    SELECT ?abstract WHERE {
    
                        <""" + uri + """> dbo:abstract ?abstract .
    
                        FILTER langMatches(lang(?abstract),'en')
                    } 
    
                    LIMIT 1
    
                    """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            return True, results["results"]["bindings"][0]["abstract"]["value"]


        except:
            description= ""
            return False, description


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

