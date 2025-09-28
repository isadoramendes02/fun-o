# # Questão 1 – Saudação personalizada (Função simples)
# def saudacao(nome):
#     print (f"Olá {nome}! Seja bem-vindo ao curso de lógica de programação.")
# saudacao("isa")

# #Questão 2 – Par ou Ímpar (Condicional + Função)
# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "impar"
# resultado= par_ou_impar(7)
# print(f"O numero é {resultado}")

#Questão 3 – Maior de dois números (Condicional)
# def maior(numero1, numero2):
#     if numero1>numero2:
#         return numero1
#     if numero2>numero1:
#         return numero2
#     else:
#         numero1=numero2 
#         return "Os numeros são iguais."
# resposta= maior(4,4)
# print(resposta)

#Questão 4 – Tabuada (Repetição)
# numero=int(input("Digite um numero:"))
# print(f"\n tabuada do {numero} \n:")
# for i in range(1,11):
#         print(f"{numero} x {i} = {numero * i}")

#Questão 5 – Contagem regressiva (Laço)
# for contagem in range(10,-1,-1):
#     print(contagem)
# print("EXPLOSÃO!!!!!")

#Questão 6 – Média de notas (Função + Repetição)
# def calcular_media():
#     quantidade_notas=int(input("Quantas notas voce quer calcular a media:"))
#     total= 0
#     for i in range (quantidade_notas):
#         nota = float(input(f"Digite {i+1}ª  nota:"))
#         total += nota
#     media= total / quantidade_notas
#     return media
# media = calcular_media()
# print(f"A media das notas é: {media}")

#Questão 7 – Fatorial (Repetição + Função)
def fatorial(n):
    for i in range(1,n + 1):
        resultado *= 1
    return resultado
print(f"O fatorial é: {fatorial}")


























