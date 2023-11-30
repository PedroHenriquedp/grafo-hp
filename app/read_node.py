import csv

# Dicionário de nomes e IDs
nomes_dict = {
    'HARRY': 1,
    'HERMIONE': 2,
    'RON WEASLEY': 3,
    'HAGRID': 4,
    'NEVILLE': 5,
    'QUIRRELL': 6,
    'PAT': 7,
    'SIR NEVILLE': 8,
    'MFRED WEASLEY': 9,
    'DUMBLEDORE': 10,
    'LILIAN POTTER': 11,
    'SNAKE': 12,
    'PEDRO PETTIGREW': 13,
    'TOM': 14,
    'DORIS': 15,
    'DRACO MALFOY': 16,
    'THE FAT LADY': 17,
    'MRS. WEASLEY': 18,
    'SEVERUS SNAPE': 19,
    'LJ': 20,
    'FIRENZE': 21,
    'HOGWART GHOSTS': 22,
    'SFRED WEASLEY': 23,
    'GRIPHOOK': 24,
    'GOBLIN': 25,
    'PROFESSOR FLITWICK': 26,
    'FRED WEASLEY': 27,
    'GINNY': 28,
    'GEORGE WEASLEY': 29,
    'DUDLEY': 30,
    'UNCLE VERNON': 31,
    'PERCY': 32,
    'VOLDEMORT': 33,
    'TOM (BARTENDER)': 34,
    'FILCH': 35,
    'WALL PICTURE': 36,
    'AUNT PETUNIA': 37,
    'OLLI': 38,
    'MCGONAGALL': 39,
    'SHARRY': 40,
    'OLIVER WOOD': 41,
    'PEDRO PETTIGREW': 42,
    'CRABBE': 43,
    'GOYLE': 44
}

# Nome do arquivo CSV de entrada
arquivo_csv_entrada = './nodes/Arestas_Edges.csv'  # Substitua pelo nome do seu arquivo CSV

# Nome do arquivo CSV de saída
arquivo_csv_saida = 'saida.csv'


# Função para substituir os nomes pelos IDs
def substituir_nomes_por_ids(nome):
    return nomes_dict.get(nome, nome)


# Abrir o arquivo CSV de entrada e criar um novo arquivo CSV de saída
with open(arquivo_csv_entrada, 'r', newline='', encoding='utf-8') as csv_entrada, \
        open(arquivo_csv_saida, 'w', newline='', encoding='utf-8') as csv_saida:
    # Criar leitores e escritores CSV
    leitor_csv = csv.reader(csv_entrada)
    escritor_csv = csv.writer(csv_saida)

    # Ler a primeira linha (cabeçalho) do arquivo de entrada
    cabecalho = next(leitor_csv)

    # Escrever o cabeçalho no arquivo de saída
    escritor_csv.writerow(cabecalho)

    # Iterar sobre as linhas restantes do arquivo de entrada
    for linha in leitor_csv:
        # Substituir os nomes pelos IDs na linha
        linha_modificada = [substituir_nomes_por_ids(nome) for nome in linha]

        # Escrever a linha modificada no arquivo de saída
        escritor_csv.writerow(linha_modificada)

print(f'A substituição foi concluída. Os resultados foram salvos em {arquivo_csv_saida}.')
