# print ("Hello world")
# print ("Guilherme")
# #print ("") = mostra o texto, apenas um print por linha
# #ctrl + ; = comenta ou descomenta o código, tem que selecionar o texto

# #diferença entre texto e número
# print (10+10) #realiza a soma
# print ("10"+"10") #concatena = junta o texto 

# # operações matemáticas
# # soma  +
# # subtração -
# # multiplicação *
# # divisão /

# #exemplos
# print (2+2)
# print (10-5)
# print (10*2)
# print (20/2)

# #para rodar o arquivo sem a setinha basta escrever python e o nome do arquivo no terminal

#PARAMETROS NO PRINT
#print (a,b, c, d, e, ...) até no máximo 128 parametros (vírgulas), usados para separar dados 
# print ("escola senai")
# print ("escola", "senai")
# print ("10 + 10 =", 10+10)

#ATIVIDADE 01

print ("Guilherme de Oliveira Pereira, 16 anos, vulgo comedor de casadas, dono do cpf 46029386808 ")
print ("Guilherme de Oliveira Pereira", "16 anos", "dono do cpf 46029386808" )

#Formatação Sep e End
#sep -> operador de separação, substitui a vírgula por o que vc quiser,pode ser qualquer merda
#precisa haver mais de um parâmetro
#end -> operador final
#coloca o caractere no final do print
#coloca a linha de baixo na mesma linha do comando de cima
#\n -> quebra a linha se colocar dentro dos parênteses 

#limpar a tela
import os
os.system("cls")

# print("#"*5, "SEJA BEM VINDO", "#"*5)
# print("aula","de", "python", sep="&",end="! \n")
# print ("no senai")

print("ATIVIDADE 2")
print("curso","de","python", sep="_", end="%% \n")
print("*no","senai","rio","claro")
print("","lógica","de","programação", sep="_-_-_")

print("ATIVIDADE 3")
print("lógica","versão3", sep="@@@", end="[] \n")
print("lógica","de","programação", sep="###")
print("","uso","do","print",sep="&",end="()" )

