import requests
import json
from SPARQLQuery import getSPARQLDescription
import time


def findPlaces(radius):
    apikey = "AIzaSyCi6jqyLCqAu5sqiAJzrme0s4PK19bo7Hg"

    names = list()
    listPOI= list()
    pagetoken = None

    lat = 52.3740300
    lng= 4.8896900
    #radius = 10000
    type = "museum"

    while True:

        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={apikey}{pagetoken}"\
            .format(lat = lat, lng = lng, radius = radius, type = type,apikey = apikey, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")

        #print(url)
        response = requests.get(url)
        res = json.loads(response.text)
        #print(json.dumps(res, indent=4, sort_keys=True))
        #print(res)
        #print("There are ", len(res["results"]), " results\n\n")

        for result in res["results"]:
            # print(json.dumps(result, indent=4, sort_keys=True ))
            listTypes= result["types"]
            poiName= str(result["name"])
            try:
                photo_reference = result['photos'][0]['photo_reference']
            except:
                photo_reference = ""

            #boolSPARQL= True
            boolSPARQL, descriptionPOI = getSPARQLDescription(poiName, listTypes)
            if(boolSPARQL and (photo_reference is not "")):

                ID_place = result['place_id']
                max_height =result['photos'][0]['height']
                max_width = result['photos'][0]['width']

                url_photo = "https://maps.googleapis.com/maps/api/place/photo?" \
                            "photoreference={photo_reference}&sensor=false&maxheight={max_height}&maxwidth={max_width}&key={APIKEY}"\
                    .format(photo_reference=photo_reference, max_height=max_height,max_width=max_width, APIKEY=apikey)

                #print(url_photo)



                url_details = "https://maps.googleapis.com/maps/api/place/details/json?" \
                              "placeid={ID_place}&fields=name,rating,formatted_phone_number,website&key={APIKEY}".format(ID_place=ID_place, APIKEY=apikey)

                responseDetails = requests.get(url_details)
                resDetails = json.loads(responseDetails.text)

                try:
                    vicinity = resDetails['result']['vicinity']
                except:
                    vicinity = ""

                try:
                    website = resDetails['result']['website']
                except:
                    vicinity=""


                tuple= (poiName, descriptionPOI, url_photo, vicinity, website )
                listPOI.append(tuple)




        pagetoken = res.get("next_page_token",None)

        if not pagetoken:
            break
        #print("\n\nhere -->> ", pagetoken)


   #return pagetoken
    return listPOI



    #delete duplicates
    names= list(set(names))

    # for i in range(len(names)):
    #     poi= getSPARQLDescription(str(names[i]))
    #
    #     if(poi != ""):
    #         print(names[i] + "\n" + poi+"\n\n")
    #
    # names= list()




tuplesArray= findPlaces(10000)

for x in tuplesArray:
    for k in range(0,5):
        print(x[k])
    print("\n")