from SPARQLWrapper import SPARQLWrapper, JSON
import json


def getSPARQLDescription(poiName):

    try:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        city= "Amsterdam"
        poiKind= "Museum"
        sparql.setQuery("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?s ?l ?d 
            WHERE {
            ?s a dbo:"""+poiKind+""" .
            ?s dbo:location dbr:"""+city+""" .
            ?s rdfs:label ?l .
            FILTER contains(lcase(str(?l)),lcase('"""+poiName+"""'))
            FILTER langMatches(lang(?l),'en')
            ?s dbo:abstract ?d .
            FILTER langMatches(lang(?d),'en')
            } 
            LIMIT 1
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        description= results["results"]["bindings"][0]["d"]["value"]
        return True, description,
    except:
        description= ""
        return False, description

#
#
# des= getSPARQLDescription("ARTIS")
# print(des)

