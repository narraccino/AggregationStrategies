import json, requests,geocoder, time
from geopy.geocoders import Nominatim
from pygeocoder import Geocoder
from getDescription import PoiDescription


def topResults():
    url = 'https://api.foursquare.com/v2/venues/search'

    #g = geocoder.ip('me')
    #location = Geocoder.reverse_geocode(g.lat,g.lng)
    #print("You are in:",location.city, ",",location.country)
    #position = str(g.lat) + ','+ str(g.lat)

    params = dict(
      client_id='5YVODSSQQZCYBSP3AHEJLRH2KUENEDSAZLBZA3XCHC0DNBO3',
      client_secret='ZHV1NYA5DQMVKTAX52TRQUJDVQXDAIXOYMIP1NWF5AR4L0SA',
      v=str(time.strftime("%Y%m%d")),
      ll='52.379189,4.899431',
      #near = 'Amsterdam',  #location.city,
      radius= 4000,
      section='topPicks',
      limit=20
    )

    print("You are in Amsterdam\n\n")
    resp = requests.get(url=url, params=params)
    json_data = json.loads(resp.text)

    #print(json.dumps(json_data, indent=5, sort_keys=True))


    num = len(json_data['response']['venues'])
    i=1
    for poi in range(num):
        print(i,'.')
        print(json_data['response']['venues'][poi]['name'],'\n')
        venue_ID= json_data['response']['venues'][poi]['id']
        #print('VENUE ID: ', venue_ID,'\n')
        PoiDescription(venue_ID)
        i=i+1





