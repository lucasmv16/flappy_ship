import json
import game

def json_score():
    #json
    # Criar um dicionário com o game.score e o progresso
    data = {
        'score': game.score,
        'progress': game.progress
    }

    # Converter o dicionário em JSON
    json_data = json.dumps(data)

    # Escrever o JSON no arquivo
    with open('game_data.json', 'w') as file:
        file.write(json_data)