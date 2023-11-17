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
    Pedra filosofal: http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-Sorcerer's-Stone.html
    Câmara Secreta: http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-Chamber-of-Secrets.html --> bugado
    Prisioneiro de Askaban: http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-Prisoner-of-Azkaban.html --> bugado
    Cálice de fogo: http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-Goblet-of-Fire.html --> funciona
    Ordem da Fênix: http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-Half-Blood-Prince.html --> bugado
    """
    print(f'pegando o estado: {movie} info...')
    movie_url = f"http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-{movie}.html"
    page = requests.get(movie_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    falas = soup.select('pre')

    for idx, fala in enumerate(falas):
        fala_texto = str(fala)
        fala_sem_html = BeautifulSoup(fala_texto, 'html.parser').get_text()
        falas[idx] = fala_sem_html

    return fala_sem_html


def format_script(script_text):
    lines = script_text. split('\n')
    formatted_script = []

    speaker = None
    speech = []

    for line in lines:
        line = line.strip()
        if line.isupper():
            if speaker and speech:
                formatted_script.append(f'{speaker}: {" ".join(speech)}')
            speaker = line
            speech = []
        else:
            speech.append(line)

    if speaker and speech:
        formatted_script.append(f'{speaker}: {" ".join(speech)}')

    return "\n".join(formatted_script)

harry_movie = "Sorcerer's-Stone"

page = scrape_historia(f"{harry_movie}")
formatted_text = format_script(page)
print(formatted_text)