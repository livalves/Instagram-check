import json
from datetime import datetime

with open('followers_and_following/followers_1.json', 'r') as file:
    seguidores_json = json.load(file) 
    
def extrair_followers(json_data):
    usernames = []
    for item in json_data:  
        for data in item["string_list_data"]:  
            usernames.append(data["value"])
    return usernames

seguidores = extrair_followers(seguidores_json)


with open('followers_and_following/following.json', 'r') as file:
    seguindo_json = json.load(file)  
    
def extrair_following(json_data):
    usernames = []
    if "relationships_following" in json_data:
        for item in json_data["relationships_following"]:  
            if "string_list_data" in item:  
                for data in item["string_list_data"]:  
                    if "value" in data:  
                        usernames.append(data["value"])
    return usernames
     
seguindo = extrair_following(seguindo_json)


seguindo_set = set(seguindo)
seguidores_set = set(seguidores)
nao_seguem_de_volta = seguindo_set - seguidores_set

data_atual = datetime.now().strftime("%d-%m-%Y")
filename = f'output/nao-seguidores_{data_atual}'
with open(filename, 'w') as file:
    for i, usuario in enumerate(nao_seguem_de_volta, start=1):  
        file.write(f"{i}. {usuario}\n")


print('-'*30)
print('Seguidores: ', len(seguidores))
print('Seguindo: ', len(seguindo))
print('Não seguidores: ', len(nao_seguem_de_volta))
print('-'*30)
print(f"Dados salvos em: {filename}")
print('-'*30)



