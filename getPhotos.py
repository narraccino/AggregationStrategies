import json


def getPhotos(json_data):
    try:
        numPics=len(json_data['response']['venue']['photos']['groups'][0]['items'])
        if(numPics>=1):
            for i in range(0,numPics):
                url= json_data['response']['venue']['photos']['groups'][0]['items'][i]['prefix'] + str('width')+ str(json_data['response']['venue']['photos']['groups'][0]['items'][i]['width']) + json_data['response']['venue']['photos']['groups'][0]['items'][i]['suffix']
                print(url)

    except:
        print('No Photos')




