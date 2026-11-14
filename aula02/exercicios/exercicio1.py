'''1) Escreva um programa que peça à pessoa usuária para fornecer dois 
números e exibir o número maior
'''

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1>n2:
    print(f'O número {n1:.0f} é maior do que o número {n2:.0f}')
    
elif n2>n1:
    print(f'O número {n2:.0f} é maior do que o número {n1:.0f}')

else:
    print(f'Os números {n1:.0f} e {n2:.0f} são iguais!')