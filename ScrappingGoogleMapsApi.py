import requests
import pandas as pd




url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Edificio%20EL%20CORAL%20Laureles&inputtype=textquery&fields=formatted_address%2Cplace_id%2Cname%2Cgeometry&locationbias=circle%3A2000%406.241222190281002%2C-75.5955602040378&key=" + apikey

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
a = response.text
print(a)




url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJP2cLTKcpRI4REvt5u7EMZKA&fields=name%2Cformatted_phone_number&key="+apikey

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)