import os
import csv
import json

pessoa = {
    "nome": "Felipe",
    "idade": 28,
    "cidade": "Salvador"
}

diretorio = os.getcwd()

caminho_csv = os.path.join(diretorio, "pessoa.csv")
caminho_json = os.path.join(diretorio, "pessoa.json")
caminho_txt = os.path.join(diretorio, "pessoa.txt")

def salvar_csv(dados, caminho):
    with open(caminho, mode="w", newline='', encoding="utf-8") as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=dados.keys())
        writer.writeheader()
        writer.writerow(dados)

def salvar_json(dados, caminho):
    with open(caminho, mode="w", encoding="utf-8") as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

def salvar_txt(dados, caminho):
    with open(caminho, mode="w", encoding="utf-8") as arquivo_txt:
        for chave, valor in dados.items():
            arquivo_txt.write(f"{chave.capitalize()}: {valor}\n")

salvar_csv(pessoa, caminho_csv)
salvar_json(pessoa, caminho_json)
salvar_txt(pessoa, caminho_txt)

print("\nDados salvos:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")

print(f"\nArquivos salvos em: {diretorio}")
