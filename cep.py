import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")

    except requests.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")

def main():
    cep = input("Digite o CEP (somente números): ").strip()

    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("CEP inválido. Digite exatamente 8 números.")

if __name__ == "__main__":
    main()
