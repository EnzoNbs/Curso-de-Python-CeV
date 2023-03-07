"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor
correto.
"""

i = 0
p = 0

print(f'\033[34mDigite "M" para Masculino\n'
      f'\033[31mDigite "F" para Feminino\n'
      f'\033[0mDigite qualquer número para finalizar\n{"-=-"*12}')

while i < i + 1:
    sx = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
    if sx.isnumeric():
        break
    elif sx not in "MmFf":
        i -= 1
        print('Opção inválida, Tente novamente.\n')
    else:
        if sx == 'M':
            print('Sexo masculino registrado com sucesso\n')
        else:
            print('Sexo feminino resgitrado com sucesso\n')
        p += 1

print('Finalizando...')
print(f'Você adicionou o sexo de {p} pessoas')

# while sx not in 'MmFf':
# sx = str(input('Dados inválidos.
# Por favor, informe seu sexo: ')).strip().upper()[0]
# print(f'Sexo {sx} registrado com sucesso')
