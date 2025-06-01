import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  
        
        dados = resposta.json()
        usuario = dados['results'][0]

        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil Gerado ===")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao acessar a API: {erro}")

gerar_usuario()
