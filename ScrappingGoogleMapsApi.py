import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os
import json

## Loads enviroment variables on .env file
load_dotenv()


apikey = os.getenv('APIKEY')
Excelfile = "DataEdificiosMedellín.xlsx"
data = pd.read_excel(Excelfile)
urlPlacesSearch = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="

payload={}
headers = {}
responses = {}



for i in range(len(data)):
    input = data['input'][i]
    lat = data['LATITUD'][i]
    long = data['LONGITUD'][i]
    id = data['ID'][i]
    url = urlPlacesSearch + input + "&inputtype=textquery&fields=formatted_address%2Cplace_id%2Cname%2Cgeometry&locationbias=circle%3A300%40" + str(lat) + "%2C" + str(long) + "&key=" + apikey
    response = requests.request("GET", url, headers=headers, data=payload)
    responseJson = json.loads(response.text)
    try:
        responses[str(id)] = responseJson['candidates'][0]
    except:
        responses[str(id)] = "Not Found"
    time.sleep(1)

urlPlacesDetail = "https://maps.googleapis.com/maps/api/place/details/json?place_id="


#url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Edificio%20EL%20CORAL%20Laureles&inputtype=textquery&fields=formatted_address%2Cplace_id%2Cname%2Cgeometry&locationbias=circle%3A300%406.241222190281002%2C-75.5955602040378&key=" + apikey


for j in range(len(responses)):
    try:
        place_id = responses[str(j+1)]['place_id']
        url = urlPlacesDetail + place_id + "&fields=formatted_phone_number&key="+apikey
        response = requests.request("GET", url, headers=headers, data=payload)
        responseJson = json.loads(response.text)
        if len(responseJson['result'])>0:
            responses[str(j+1)]['phone_number'] = responseJson['result']['formatted_phone_number']
        else:
            responses[str(j+1)]['phone_number'] = "0"
    except:
        print("place_id not found")
    time.sleep(1)

with open("responses.json", "w") as outfile:
    json.dump(responses, outfile, indent=4)