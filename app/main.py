import json

with open("characters.json", encoding='utf-8') as personagem:
    allchar = json.load(personagem)

contador = 0
for personagem in allchar:
    if personagem['actor'] != '':
        personagemfic = personagem['name']
        contador += 1
        print(f'{personagemfic} {contador}')