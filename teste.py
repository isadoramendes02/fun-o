#modelo basico
def saudacao(nome):
    return (f"Olá {nome} Seja bem-vindo ao mundo python!")
print(saudacao("isa"))

#Outra forma
def saudacao(nome):
    print (f"Olá {nome} Seja bem-vindo ao mundo python!")
saudacao("isa")

#Utilizando "return"
def soma(a, b):
    return a+b
resposta= soma(5,5)
print("A soma é:",resposta)

#Crie uma função que receba um nome e
# imprima uma saudação personalizada.
def saudacao(nome):
    print (f"Olá {nome} Seja bem-vindo(a) ao mundo python!")
saudacao("isa")

#Crie uma função que receba dois
# números e imprima o maior deles.
def maior(numero1, numero2):
   if numero1 > numero2:
       return numero1
   if numero2 > numero1:
       return numero2
resposta= maior(23, 20)
print(f"O numero maior é: {resposta}")

# Com igual
def maior(numero1, numero2):
   if numero1 > numero2:
       return numero1
   if numero2 > numero1:
       return numero2
   else:
       numero1 = numero2
       return "Os numeros são iguais"
resposta= maior(20, 20)
print(resposta)

#Crie uma função que receba um número
#e retorne se ele é par ou ímpar.
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
resultado= par_ou_impar(10)
print(f"O numero é: {resultado}")

































































































def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
resultado= par_ou_impar(20)
print(f"O numero é : {resultado}")