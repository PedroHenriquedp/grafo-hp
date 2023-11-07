import json

def read_personagem():
    """Função para ler o arquivo de personagens da API https://hp-api.onrender.com/api/characters"""
    with open("characters.json", encoding='utf-8') as personagem:
        allchar = json.load(personagem)
    return allchar

def create_dict_allchar():
    """Função para fazer um scrape nos personagens e criar um dicionário próprio"""
    allchar = read_personagem()

    dic_personagem = []

    for personagem in allchar:
        thisdic_personagem = {
            "nome": personagem["name"],
            "especie": personagem["species"],
            "genero": personagem["gender"],
            "casa": personagem["house"],
            "data_nascimento": personagem["dateOfBirth"],
            "ano_nascimento": personagem["yearOfBirth"],
            "mago": personagem["wizard"],
            "ancestralidade": personagem["ancestry"],
            "estudante_hogwarts": personagem["hogwartsStudent"],
            "staff_hogwarts": personagem["hogwartsStaff"],
            "ator_a": personagem["actor"],
            "imagem": personagem["image"]
        }
        dic_personagem.append(thisdic_personagem)

    return dic_personagem

# def






    # contador = 0
    # for personagem in allchar:
    #     if personagem['actor'] != '':
    #         personagemfic = personagem['name']
    #         contador += 1
    #         print(f'{personagemfic} {contador}')