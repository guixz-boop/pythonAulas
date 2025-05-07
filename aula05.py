import os 
os.system("cls")
# #IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
# #ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO


# # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# #Atividade 01
# #replace("valor1","valor2") ->Substitui o valor1 pelo valor2
# n1 = float(input("Digite a primeira nota: ").replace(",","."))
# n2 = float(input ("Digite a segunda nota: ").replace(",","."))
# media = (n1+n2)/2

# #:.2f -> formata para 2 casas decimais, apenas no fstring
# if media < 5:
#     print (f"Média: {media:.2f}.REPROVADO")
# elif media <=7:
#     print (f"Média: {media:.2f}. Em recuperação")
# elif media > 7:
#     print(f"Média: {media:.2f}. APROVADO")

# #Atividade 02
# p = float(input("Digite o seu peso: ").replace(",","."))
# a = float(input("Digite a sua altura: ").replace(",","."))
# imc = round((p / (a ** 2)),2)

# print(f"Seu imc é {imc}")
# if imc < 17:
#     print ("Muito abaixo do peso")
# elif imc <= 18.49:
#     print ("Abaixo do peso")
# elif imc <= 24.99:
#     print ("Peso normal")
# elif imc <= 29.99:
#     print ("Acima do peso")
# elif imc <= 34.99:
#     print ("Obesidade 1")
# elif imc <= 39.99:
#     print ("Obesidade 2")
# else:
#     print ("Obesidade 3 (mórbida)")

#Atividade 03
print("="*15,"AUTOCAR","="*15)
print(r"""
     ___________________¶¶
____________________¶¶__¶_5¶¶
____________5¶5__¶5__¶¶_5¶__¶¶¶5
__________5¶¶¶__¶¶5¶¶¶¶¶5¶¶__5¶¶¶5
_________¶¶¶¶__¶5¶¶¶¶¶¶¶¶¶¶¶__5¶¶¶¶5
_______5¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶_5¶¶__5¶¶¶¶¶5
______¶¶¶¶¶5_¶¶¶¶¶¶¶¶¶¶¶¶¶5¶¶¶__¶¶¶¶5¶5
_____¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶5
____¶¶¶¶¶¶¶_¶¶¶5¶¶¶¶5_¶¶¶¶¶5_5¶_¶¶¶¶¶¶¶¶5
___¶¶¶¶¶¶¶¶__5¶¶¶¶¶¶5___5¶¶¶¶__5¶¶¶¶¶¶¶¶¶5
__¶¶¶¶¶¶¶¶¶¶5__5¶¶¶¶¶¶5__5¶¶5_5¶¶¶¶¶¶¶¶¶¶¶
_5¶¶¶¶¶¶¶¶¶¶¶¶_5¶¶¶¶¶¶¶¶¶5__5¶¶¶¶¶¶¶¶¶¶¶¶¶5
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_5¶¶¶¶
5¶¶¶¶¶¶¶¶¶¶¶¶5___5¶¶¶¶¶¶¶5__¶¶¶¶5_¶¶¶5_¶¶¶¶
¶¶¶¶¶¶¶¶_¶¶5_5¶5__¶¶¶¶¶¶¶¶¶5_5¶¶¶_5¶¶¶_5¶¶¶5
¶5¶¶¶¶¶5_¶¶_5¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶5_5¶¶_5¶¶¶_¶¶¶5
¶¶¶¶_¶¶__¶__¶¶¶¶¶¶5_5¶¶¶¶¶¶¶¶¶¶5_¶¶_5¶¶_5¶¶¶
¶¶¶5_5¶______5¶¶5¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶5_¶¶_5¶5_¶5¶
5¶¶____5¶¶¶¶5_____5¶¶¶¶¶¶¶5_¶¶¶¶¶5_¶__¶¶_5¶¶
_¶¶__5¶¶¶¶¶¶¶¶¶¶5____5¶¶¶¶¶¶_¶¶¶¶¶_____¶5_¶¶
_¶¶___5¶¶¶¶¶¶¶¶¶__________5¶5_¶¶¶¶¶____¶¶_¶¶
_¶¶_______5¶¶¶¶¶¶5____________¶¶¶¶¶_____¶_¶¶
_5¶5________5¶¶_¶¶¶¶5________5¶¶¶¶¶_______¶¶
__¶¶__________¶___¶¶¶¶¶5___5¶¶¶¶¶¶5_______¶5
__¶¶____________5¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶
___¶________________5¶¶¶¶¶¶¶¶5_¶¶
___¶__________5¶¶¶¶¶¶¶¶5¶¶¶5__5¶5
_____________________5¶¶¶5____¶5 
    
      
      """)
print ("-"*15,"TABELA DE REAJUSTES DO SALÁRIO","-"*15,"\n")
print("Salários até R$2799,99: aumento de 20%")
print("Salários entre R$2800,00 e R$6999,99: aumento de 15%")
print("Salários entre R$7000,00 e R$14.999,99: aumento de 10%")
print("Salários de R$ 15.000,00 em diante: aumento de 5%\n")

s = float(input("Digite seu salário: "))

if s <= 2799.99:
    p = "20%"
    r = (s * 0.2) + s
elif s <= 6999.99:
    p = "15%"
    r = (s * 0.15) + s
elif s <= 14999.99:
    p = "10%"
    r = (s * 0.1) + s
elif s >= 15000.00:
    p = "5%"
    r = (s * 0.05) + s

print(f"O salário antes do reajuste era de: {s}")
print(f"O percentual do aumento foi de: {p}")
print(f"O valor do aumento foi de: ",r - s)
print("Novo salário:", r)