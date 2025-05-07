import os
os.system("cls")

#Continuação Input com Int e Float
#por padrão o input retorna o que foi digitado como string
#type -> função que retorna o tipo de dado
#int() -> converte para inteiro
#float() -> converte para numero quebrado

#exemplo 1 
# numero = 10
# numero2 = int(input("digite um numero: "))
# print ("o tipo de número é,", type (numero2))
# soma = numero + numero2
# print(f"soma de {numero} + {numero2} = ",soma)

# #exemplo 2
# num1 = input("digete um numero: ")
# soma = int(num1) + 10
# print("A soma de",num1,"+","15","=",soma)

# #exemplo 3
# n1 = input("digite um número: ")
# n2 = input("digite outro numero: ")
# soma = int(n1)+int(n2)

# print(f"a soma de {n1} + {n2} = ", soma)

# #ATIVIDADE 01
# n1 = int(input("digite um numero: "))
# n2 = int(input("digite outro numero: "))
# produto = (n1) * (n2)
# print(f"A multiplicação desses números é {produto}")

# #ATIVIDADE 02
# n1 = int(input("digite um número: "))
# a = n1 - 1
# s = n1 + 1
# print(f"Você escolheu o número {n1}, o antecessor desse número é {a} e o sucessor é {s}")

# #ATIVIDADE 03
# n1 = int(input("digite o ano em que você nasceu: "))
# idade = 2025 - n1
# print (f"Você tem {idade} anos")

#ATIVIDADE 04
print ("="*15,"SUPERMERCADO","="*15)

item1 = input("Qual é o produto? ")
v1 = float(input(f"Quanto custa o {item1}? "))
item2 = input("Qual é o outro produto? ")
v2 = float(input(f"Quanto custa o {item2}? "))

print("-"*30)

print("="*15,"Caixa","="*15)
vd = v1 * 0.1
vd2 = v2 * 0.25
f1=round (v1 - vd,2)
f2=round (v2 - vd2,2)
print(f"O {item1} custa {v1}, mas com 10% de desconto sai",v1 - vd)
print(f"O {item2} custa {v2}, mas com 25% de desconto sai",v2 - vd2)

print("-"*30)

print("TOTAL R$: ", round (f1 + f2, 2))

#round(valor,quantidade de casas decimais), obs: só pode usar dois parâmetros
