import os
os.system("cls")

#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)


# # #ATIVIDADE 01 / 02
# idade = int(input("Qual a sua idade? "))
# if idade >= 18:
#     if idade < 120:
#         print ("Você é maior de idade")
#     else:
#         print ("Idade invália")
# else:
#     if idade > 0:
#         print ("Você é menor de idade")
#     else:
#         print ("Idade inválida")

#ATIVIDADE 03
# email = input("Digite seu email: ").lower() #lower e upper = serve para transformar o texto inteiro em caixa alta ou minúsculo, utilizado para fazer comparações
# senha = input("Digite a senha do email: ")
# if email == "python@senai.com" and senha == "12345678":
#     print ("Usuário autenticado")
# else:
#     print("Usuário ou senha inválidos")

# #ATIVIDADE 4
# quantidade = int(input("Quantas maçãs você vai querer? "))
# if quantidade < 12:
#     valor = 0.30
# else:
#     valor = 0.25
# total = round(quantidade*valor,2)
# print(f"Você comprou {quantidade} maçãs, cada maçã saiu por R${valor} e você irá pagar {total}") 

#ATVIDADE 5 
# letra = input("Digite uma letra: ").lower()
# if letra == "a" or letra == "e" or letra == "i" or letra == "u" or letra == "o":
#     print (f"A letra {letra} é vogal")
# else:
#     print (f"A letra {letra} é consoante")

#ATIVIDADE 6
# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))
# if n1 > n2:
#     print("O maior número é: ",n1)
#     print("O menor número é: ",n2)
# else:
#     print("O maior número é: ",n2)
#     print("O menor número é: ",n1)

#OPERADOR in -> usado para fazer condicional se algo estiver dentro de determinado texto é verdadeiro
#só funciona para texto, pega os dígitos
# letra = input("Digite uma letra: ")
# if letra in "aeiouAEIOU":
#     print ("É vogal")
# else:
#     print("É consoante")