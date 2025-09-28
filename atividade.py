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

# #Questão 7 – Fatorial (Repetição + Função)
# numero = int(input("Digite um número para que seja exibido seu fatorial:"))
# fatorial = 1
# for i in range(1, numero + 1):
#     fatorial *= i
# print(f"O fatorial de {numero} é {fatorial}")


# #Questão 8 – Verificar vogais (Função + String)
# ContarVogais = input("Digite uma palavra:")
# vogais = "aeiou"
# contador = 0
# for letra in ContarVogais :
#     if letra in vogais:
#         contador += 1
# print(f"A palavra {ContarVogais} possui {contador} vogais.")


# #Questão 9 – Jogo de adivinhação (Laço + Condicional)
# def jogo_adivinhacao():
#     numero_secreto = 7
#     chute = 0
#     tentativas = 0
#     print("Jogo de Adivinhação")
#     while chute != numero_secreto:
#         chute = int(input("Digite um número entre 1 e 10: "))
#         tentativas += 1
#         if chute == numero_secreto:
#             print(f"Parabéns! Você acertou em {tentativas} tentativas!")
#         elif chute < numero_secreto:
#             print("O número é MAIOR. Tente novamente.")
#         else:
#             print("O número é MENOR. Tente novamente.")
# jogo_adivinhacao()


# #Questão 10 – Soma dos pares (Laço + Condicional)
# soma_pares = 0
# for _ in range(int(input("Quantos números?: "))):
#     n = int(input("Digite um número inteiro: "))
#     if n % 2 == 0:
#         soma_pares += n
# print(soma_pares)


# #Questão 11 – Função calculadora (Função + Condicional)
# def calculadora(num1,num2,operacao):
#     num1 = float(input("Digite o primeiro valor: "))
#     num2 = float(input("Digite o segundo valor: "))
#     operacao = input("Escolha uma operação: +, -, /, *: ")
#     if operacao ==  "+":
#        return num1 + num2
#     elif operacao == "-":
#        return num1 - num2
#     elif operacao == "*":
#        return num1 * num2
#     elif operacao == "/":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Erro: divisão por zero!"
#     else:
#         return "Operação inválida!"
# print(calculadora(0,0,""))


# #Questão 12 – Verificar primo (Função + Laço)
# def primo(n):
#     if n < 2:
#         return False  
#     for i in range(2, n):
#         if n % i == 0:
#             return False  
#     return True  
# num = int(input("Digite um número: "))
# if primo(num):
#     print(f"{num} é primo!")
# else:
#     print(f"{num} não é primo!")


# #Questão 13 – Inverter palavra (Função + String)
# def inverter_palavra(palavra):
#   return palavra[::-1]


# palavra = input("Digite uma palavra: ")
# palavra_invertida = inverter_palavra(palavra)
# print(f"A palavra original é: {palavra}")
# print(f"A palavra invertida é: {palavra_invertida}")


#Questão 14 – Contar pares e ímpares (Laço + Condicional)
# Quantidade = int(input("Quantos números deseja digitar?: "))


# pares = 0
# impares = 0


# for i in range(Quantidade):
#     n = int(input(f"Digite o {i+1}º número: "))
#     if n % 2 == 0:
#         pares += 1
#     else:
#         impares += 1


# print("Quantidade de pares:", pares)
# print("Quantidade de ímpares:", impares)


























