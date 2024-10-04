def calcula_dobro(x):
    dobro = x * 2
    triplo = x * 3
    return dobro, triplo
    


    



num = float(input('Informr o número: '))

x2, x3 = calcula_dobro(num)

print(f'O dobro é {x2} e o triplo é {x3}')