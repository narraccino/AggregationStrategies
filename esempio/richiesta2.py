import requests
import json


APIKEY = "AIzaSyCi6jqyLCqAu5sqiAJzrme0s4PK19bo7Hg"
loc=("52.3740300","4.8896900")
radius=10000
pagetoken = None
lat, lng = loc
type = "museum"
#=list()
#typeList.append("aquarium","art_gallery", "church", "zoo", "stadium", "amusement_park", "point_of_interest", "park", "museum")
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}"\
       .format(lat = lat, lng = lng, radius = radius, type = type,APIKEY = APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
#print(url)
response = requests.get(url)
res = json.loads(response.text)
#print(json.dumps(res, indent=4, sort_keys=True ))

photo_reference= res['results'][0]['photos'][0]['photo_reference']
max_height= res['results'][0]['photos'][0]['height']
max_width= res['results'][0]['photos'][0]['width']

ID_place= res['results'][0]['place_id']
name_place= res['results'][0]['name']
rating = res['results'][0]['rating']
vicinity = res['results'][0]['vicinity']

url_photo= "https://maps.googleapis.com/maps/api/place/photo?photoreference={photo_reference}&sensor=false&maxheight={max_height}&maxwidth={max_width}&key={APIKEY}".format(photo_reference= photo_reference,max_height=max_height, max_width=max_width, APIKEY=APIKEY)

print(url_photo)


url_details= "https://maps.googleapis.com/maps/api/place/details/json?" \
             "placeid={ID_place}&fields=name,rating,formatted_phone_number,website&key={APIKEY}".format(ID_place=ID_place,APIKEY=APIKEY)



response = requests.get(url_details)
res = json.loads(response.text)
website= res["result"]["website"]
#print(json.dumps(res, indent=4, sort_keys=True ))
print(website)



