import json

obj_1 = {
                    "nameGroup": "TUDELFT","numTotal": 3 ,"numRemaining": 2, "state": "RED", "rows":1
        }

obj_2 = {
    "nameGroup": "POLIBA", "numTotal": 3, "numRemaining": 1, "state": "YELLOW", "rows": 1
}

# jsonData= {}
text=json.dumps(obj_1, sort_keys=True, indent=4)
text2= json.dumps(obj_2, sort_keys=True, indent=4)

data={}
data['infoGroups']=[]
data['infoGroups'].append(text)
data['infoGroups'].append(text2)

print(json.dumps(data, indent=4, sort_keys=True))