import os

os.system('cls')


def valor_multa(i):
    b = (i - 100) * 4
    return b 


# inicia o programa

limite_de_peso = 100


p = int(input('Digite o peso dos peixes: '))

if p > limite_de_peso:
    multa = valor_multa(p)
    
    
    print(f'Pague a multa {multa}')
else:
    print(f'Isento')





