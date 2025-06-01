import random
import string

def criar_password(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    for i in range(tamanho - 4):
        password.append(random.choice(caracteres))

    random.shuffle(password)
    return ''.join(password)

def main():
    print("Criador de Senhas Fortes")
    print("----------------------------")

    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo de 4 caracteres): "))
            if tamanho < 4:
                print("A senha deve ter pelo menos 4 caracteres")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    password = criar_password(tamanho)
    print("\nSua senha gerada é:", password)

if __name__ == "__main__":
    main()
