import json
import os
import requests
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
    """SCRAPE DO ROTEIRO EM INGLÊS DE TODOS OS FILMES DO HARRY POTTER"""
    print(f'Pegando informações sobre {movie}...')
    movie_url = f"http://nldslab.soe.ucsc.edu/charactercreator/film_corpus/film_20100519/all_imsdb_05_19_10/Harry-Potter-and-the-{movie}.html"
    try:
        page = requests.get(movie_url)
        page.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter página: {e}")
        return None

    soup = BeautifulSoup(page.content, 'html.parser')
    falas = soup.select('pre')

    for idx, fala in enumerate(falas):
        fala_texto = str(fala)
        fala_sem_html = BeautifulSoup(fala_texto, 'html.parser').get_text()
        falas[idx] = fala_sem_html

    return fala_sem_html


def format_script(script_text):
    lines = script_text.split('\n')
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

if page:
    formatted_text = format_script(page)
    print(formatted_text)

    # Verifica se o arquivo existe e o exclui se existir
    file_path = "script_harry_stone.txt"

    try:
        # Tenta excluir o arquivo se existir
        os.remove(file_path)
        print(f"Arquivo {file_path} removido com sucesso.")
    except FileNotFoundError:
        # Se o arquivo não existir, apenas imprime uma mensagem
        print(f"Arquivo {file_path} não encontrado.")

    # Cria o arquivo e escreve o conteúdo
    with open(file_path, "w", encoding='utf-8') as file:
        content_to_write = formatted_text
        file.write(content_to_write)

    print(f"Arquivo {file_path} criado e conteúdo adicionado.")
