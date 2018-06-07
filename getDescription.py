import json, requests,geocoder, time, wikipedia
from getPhotos import getPhotos
from getSPARQLDescription import getSPARQLDescription

def PoiDescription(venue_ID,name):
    url_inc= 'https://api.foursquare.com/v2/venues/'
    url = url_inc+ venue_ID
    #print('Venue ID: ',venue_ID)

    params = dict(
        client_id='5YVODSSQQZCYBSP3AHEJLRH2KUENEDSAZLBZA3XCHC0DNBO3',
        client_secret='ZHV1NYA5DQMVKTAX52TRQUJDVQXDAIXOYMIP1NWF5AR4L0SA',
        v=str(time.strftime("%Y%m%d"))
    )

    resp = requests.get(url=url, params=params)
    json_data = json.loads(resp.text)
    #print(json.dumps(json_data, indent=5, sort_keys=True))

    try:
        category= json_data['response']['venue']['categories'][0]['shortName']
        #print(wikipedia.summary(name))
        # print(getSPARQLDescription(name))
        #print('CATEGORY: ', category, '\n\n')
        getPhotos(json_data)
    except:
        #print('CATEGORY: ', category, '\n\n')
        print("")
    return category



