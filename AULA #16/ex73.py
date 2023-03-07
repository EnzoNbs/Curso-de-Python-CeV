"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times. b) Os últimos 4 colocados.
c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
"""

tabela = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',\
    'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América',\
    'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceará',\
    'Goianiense', 'Avaí', 'Juventude'

print(f'Os time são: {tabela}\n')
print(f'A) Os cinco primeiros colocados: {tabela[:5]}')
print(f'B) Os últimos quatro colocados: {tabela[-4:]} ')
print(f'C) Times em ordem alfabética: {sorted(tabela)}')
print(f'D) Em que posição está o melhor'
      f' time Brasileiro: {tabela.index("Corinthians") + 1}º Lugar')

# D) alterado para procurar o Corinthians porque Chapecoense não estava na
# primeira divisão em 2022
