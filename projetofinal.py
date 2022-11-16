import requests
import json

parameters = {
    "flag": 'BR'
}

response = requests.get("https://airlabs.co/api/v9/flights?api_key=8714e639-5b92-48f5-849c-5219fabe0bf6", params=parameters)
arquivo = open("reply.txt" , "w+")
count = 0
lista = json.loads(response.content)
cias = lista['response']
for i in cias:
        print(count)
        print(lista['response'][count]['flag'])
        count = count+1
        
print(count , file=arquivo)