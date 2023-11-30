def read_script(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  # Ignorar a primeira linha

    characters = set()

    for line in lines:
        if ':' in line:
            character = line.split(':')[0].strip().upper()
            characters.add(character)

    return characters

def main():
    file_path = "script_harry_stone_snapshot.txt"
    characters = read_script(file_path)

    print("Personagens do Filme:")
    for character in characters:
        print(character)

if __name__ == "__main__":
    main()
