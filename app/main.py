import json
import requests
import re
from bs4 import BeautifulSoup

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

def scrape_historia(movie: str):
    """SCRAPE DO ROTEIRO EM INGLÊS DE TODOS OS FILMES DO HARRY POTTER
    Pedra filosofal: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone/Transcript
    Câmara Secreta: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Chamber_of_Secrets/Transcript
    Prisioneiro de Askaban: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Prisoner_of_Azkaban/Transcript
    Cálice de fogo: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Goblet_of_Fire/Transcript
    Ordem da Fênix: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Order_of_the_Phoenix/Transcript
    Enigma do Príncipe: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Half-Blood_Prince/Transcript
    Relíquias da morte parte 1: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Deathly_Hallows_–_Part_1/Transcript
    Relíquias da morte parte 2: https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Deathly_Hallows_–_Part_2/Transcript
    """
    print(f'pegando o estado: {movie} info...')
    movie_url = f'https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_{movie}/Transcript'
    page =  requests.get(movie_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    falas = soup.select('#mw-content-text p, #mw-content-text dd')

    # Remover os colchetes e seu conteúdo
    padrao_colchetes = r"\[[^\]]+\]"
    remover_html = r"<\/?(p|dd|i|b)>"

    regex_clean = f"({padrao_colchetes}|{remover_html})"
    for idx, fala in enumerate(falas):
        fala_texto = str(fala)
        fala_sem_colchetes = re.sub(regex_clean, '', fala_texto)
        falas[idx] = BeautifulSoup(fala_sem_colchetes, 'html.parser')

    return falas

page = scrape_historia('Half-Blood_Prince')

print(page)





    # contador = 0
    # for personagem in allchar:
    #     if personagem['actor'] != '':
    #         personagemfic = personagem['name']
    #         contador += 1
    #         print(f'{personagemfic} {contador}')