from SPARQLWrapper import SPARQLWrapper, JSON
import json

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# l='52.379189,4.899431'
city= "Amsterdam"
poiKind= "Museum"
poi="eye"

sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?s ?l ?d 
    WHERE {
    ?s a dbo:"""+poiKind+""" .
    ?s dbo:location dbr:"""+city+""" .
    ?s rdfs:label ?l .
    FILTER contains(lcase(str(?l)),lcase('"""+poi+"""'))
    FILTER langMatches(lang(?l),'en')
    ?s dbo:abstract ?d .
    FILTER langMatches(lang(?d),'en')
    } 
    LIMIT 1
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# for result in results["results"]["bindings"]:
#     print(result["label"]["value"])

print(json.dumps(results, indent=5, sort_keys=True))

# print(results["results"]["bindings"][0]["d"]["value"])

