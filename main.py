# Agenda de contatos.
from time import sleep
import csv
import os

def linha():
  print("=" * 50)

usuario = str(input("Digite um nome de Usuário: "))
sleep(1)
print("=" * 50)
print(f"Seja Bem-Vindo(a) {usuario}")
sleep(1)

while True:

  print("O que você deseja Fazer?")
  print("""
       1. Adicionar um Contato
       2. Visualizar um Contato Salvo
       3. Excluir um Contato
       \033[31m4. Sair\033[m
       """)
  escolha = int(input(": "))
  linha()

  if escolha == 1:
    nom = str(input("Nome: "))
    num = str(input("Número: "))
    mail = str(input("E-mail: "))
    alo = {nom, num, mail}
    arquivo = nom + ".csv"
    with open(arquivo, 'x') as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=',')
      csv_writer.writerow(alo)
      linha()
      print("Contato salvo com Sucesso!")

  if escolha == 3:
    nom = str(input("Digite o nome completo do contato: "))
    arquivo = nom + ".csv"
    if os.path.exists(arquivo):
      os.remove(arquivo)
      print("Contato excluido com sucesso!")
    else:
      print(f"{nom} Não é um contato existente!")

  if escolha == 2:
    nom = str(input("Digite o nome completo do contato: "))
    arquivo = nom + ".csv"
    if os.path.exists(arquivo):
      with open(arquivo, newline='') as MF:
        reader = csv.reader(MF)
        for row in reader:
          print(row)
    else:
      print(f"{nom} Não é um contato existente!")

  if escolha == 4:
    print("\033[31mSaindo", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    exit()
