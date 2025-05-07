import os
os.system("cls")

#AULA 02 -> VARIÁVEIS,TIPOS,INPUT
# variável= armazena valor 
# tem que dar nome a ela
# não pode começar com número

#Tipos de dados
#String -> texto
#Int -> n° inteiro
#Float -> n° quebrado (flutuantes)

# #declaração de variáveis
# escola = "senai"
# #mostrando o valor da variável no print 
# #concateando com o +
# print ("o nome da minha escola é" + escola)
# #separando por parametro
# print("o nome da minha escola é", escola)
# #f string {} -> mostra o valor da variável
# print(f"o nome da minha ecola é {escola}")
# #não esqueça das chaves na variável

# número = 100
# print("somando com 10",10+número)
# print("subtraindo 5 =", número -5)
# print("dividindo por 2 =", número/2)
# print("multiplicando por 10 =", número*10)

# nome="Guilherme "
# idade= "16"
# cpf= 46029386808
# print (nome,",",idade,",",cpf)

#input, comando para armazenar um valor na variável
#obrigatoriamen
# ex=input("Digite algo:")
# print(f"você dgitou {ex}")

#ATIVIDADE 1
print("*"*15,"CADASTRO","*"*15)
nome= input("Digite seu nome:")
cpf= input("Digite seu CPF:")
rg=input("Digite seu RG:")
print("*"*15,"DADOS CADASTRADOS","*"*15)
print(f"NOME:{nome}\nCPF:{cpf}\nRG:{rg}")
