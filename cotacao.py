import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada ou código inválido.")
            return

        cotacao = dados[chave]

        print(f"\nCotação {moeda} para BRL:")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Valor máximo do dia: R$ {cotacao['high']}")
        print(f"Valor mínimo do dia: R$ {cotacao['low']}")
        print(f"Última atualização: {cotacao['create_date']}")

    except requests.RequestException as e:
        print(f"Erro ao consultar a cotação: {e}")

def main():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()

    if len(moeda) == 3 and moeda.isalpha():
        consultar_cotacao(moeda)
    else:
        print("Código inválido. Use 3 letras (ex: USD).")

if __name__ == "__main__":
    main()
