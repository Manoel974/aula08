import random 

import os


def limpa_tela():
    os.system('cls')



def decoracao():
    print(12*'=')


def soma(a, b):



    return a + b 



def subtracao(a, b):



    return a - b

def multiplicacao(a, b):


    return a * b 


def divisao(a, b):
  return a / b 


def somar(a, b):
   total = a + b
   return total


def gerar_numeros():
    a = random.randint(1, 10)
    b =  random.randint(1, 10)
    return a, b 

# inicio do programa
limpa_tela() 
decoracao()
print('CALCULADORA')

a, b = gerar_numeros()
total = somar(a, b)
print(f'{a} {b} A soma é {total}')


a, b = gerar_numeros()
total = divisao(a, b)
print(f'{a} {b} A divisão é {total}')

a, b = gerar_numeros()
total = multiplicacao(a, b)
print(f' {a} {b} A multiplicação é {total}')

a , b = gerar_numeros()
total = subtracao(a, b)
print(f' {a} {b} A subtração é {total}')
