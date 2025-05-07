import os 
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#ESTRUTURA DE USO
#match valor:
#      case valor:


# linguagem = "java"

# match linguagem:

#     case "python":
#         print("é fácil")
#     case "java":
#         print("eu não fecho com a droga do diabo!")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan não dorme")
#     case 10:
#         print("entrou aqui")
#     case _ :
#         print("manda aúdio chorando")

# print ("1 = SEGUNDA")
# print ("2 = TERÇA")
# print ("3 = QUARTA")
# print ("4 = QUINTA")
# print ("5 = SEXTA")
# print ("6 = SÁBADO")
# print ("7 = DOMINGO")

# dia = int(input("Digite o número do dia da semana: "))
# match dia:
#     case 1:
#         print("SEGUNDA")
#     case 2:
#         print("TERÇA")
#     case 3:
#         print("QUARTA")
#     case 4:
#         print("QUINTA")
#     case 5:
#         print("SEXTA")
#     case 6:
#         print("SÁBADO")
#     case 7:
#         print("DOMINGO")
#     case _ :
#         print("Você é ")


# print ( "="*15,"MUNDO DO CELULAR","="*15,"\n")
# print ("="*15,"OPÇÕES DE CELULARES","="*15,"\n")

# print ("""
# 1 = XIOMI -> R$2000,00
# 2 = IPHONE -> R$3000,00
# 3 = SAMSUNG -> R$5000,00
#        \n""")

# print ("="*15,"OPÇÕES DE FRETE","="*15,"\n")
# print ("""
# 1 = SC -> R$10,00
# 2 = MG -> R$15,00
# 3 = SP -> R$20,00
#        \n""")

# cel = int(input("Digite o número do celular que você deseja: "))
# frete = int(input("Digite o número do frete: "))

# match cel:
#     case 1:
#         preço = 2000
#     case 2:
#         preço = 3000
#     case 3:
#         preço = 5000

# match frete:
#     case 1:
#         frete = 10
#     case 2:
#         frete = 15
#     case 3:
#         frete = 20

# print ("*"*40, "\n")
# print (f"PREÇO R$: {preço}")
# print (f"FRETE R$: {frete} ")
# print (f"TOTAL R$: {preço + frete}")

import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

print ("JOGO DE PEDRA, PAPEL OU TESOURA")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

player = input("Escolha pedra, papel ou tesoura: ").lower()
print(F"O PLAYER ESCOLHEU {player}")
match player:
    case "papel":
        player = papel
    case "pedra":
        player = pedra
    case "tesoura":
        player = tesoura
    case _:
        print ("O ANIMAL É PEDRA, PAPEL OU TESOURA, ESCOLHA NOVAMENTE")
        quit()

bot = random.randint(1,3)
match bot:
    case 1:
        bot = papel
    case 2:
        bot = pedra
    case 3:
        bot = tesoura

print(f"VOCÊ ESCOLHEU  {player}")
print(f"O BOT ESCOLHEU {bot}")

partida = ""

match partida:
    case _ if player == bot:
        print("DEU EMPATE")
    case _ if player == papel and bot == pedra:
        print("VOCÊ GANHOU")
        os.system ("color 2")
    case _ if player == tesoura and bot == papel:
        print("VOCÊ GANHOU")
        os.system ("color 2")
    case _ if player == pedra and bot == tesoura:
        print("VOCÊ GANHOU")
        os.system ("color 2")
    case _ :
        print ("VOCÊ PERDEU")
        os.system("color 4")



