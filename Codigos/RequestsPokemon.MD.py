import requests

url = "https://pokeapi.co/api/v2/ability/battle-armor"
dados = requests.get(url).json()

for d in dados['effect_entries']:
    if d['language']['name'] == "en":
        print(d['short_effect'])
        
#Esse programa de raspagem de dados, demonstra um exemplo de elementos em conjuntos,
#buscando da API de pokemon o elemento nome dentro do conjuntos inseridos em conjuntos