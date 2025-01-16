import json

def convertStringToJson(data:str)->dict:
    return json.loads(data)