"""
Crie um código em Python que teste se o site pudim está acessível pelo
computador usado.
"""
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não esta acesivel!')
else:
    print('Site pode ser acessado!')
    print(site.read())