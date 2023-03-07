"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela
abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

height = float(input('Digite seu tamanho: (cm) '))
weight = float(input('Digite seu peso: (Kg) '))

imc = weight/(height/100) ** 2
print(f'\033[34mIMC: {imc:.1f}')

if imc < 18.5:
    print('Status: \033[1:36mAbaixo do peso')
elif 18.5 <= imc < 25:
    print('Status: \033[1:32mPeso Ideal')
elif 25 <= imc < 30:
    print('Status: \033[1:33mSobrepeso')
elif 30 <= imc < 40:
    print('Status: \033[1:91mObesidade')
else:
    print('Status: \033[1:35mObsidade mórbida')
