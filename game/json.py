import json
import game
import os

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
    
    file.close()

def perm_json():
    permexits = os.path.exists('game_perm_data.json')
    
    data = {}
    if permexits == True:
        with open('game_perm_data.json', 'r') as file:
            json_data = file.read()

            # Converter o JSON de volta para um dicionário
        data = json.loads(json_data)
        file.close()
    update = False
    
    try:
        best_score = data["score"]
    except:
        best_score = [game.score]
        update = True

    best_score.sort(reverse=True)
    for i in range(len(best_score)):
        if not update:
            if best_score[i] < game.score and len(best_score) >= 5:
                best_score.append(game.score)
                best_score.sort(reverse=True)
                best_score.pop()
                update = True
            elif len(best_score) < 5:
                best_score.append(game.score)
                update = True
    best_score.sort(reverse=True)
    data["score"] = best_score
    # Converter o dicionário em JSON
    json_data = json.dumps(data)

    # Escrever o JSON no arquivo
    with open('game_perm_data.json', 'w') as file:
        file.write(json_data)
    
    file.close()