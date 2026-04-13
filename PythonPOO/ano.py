#faça um programa que leia um ano qualquer e diga se ele é bissexto informe que tipo de ano é se for comum informe que tipo de ano é e diga quantos dias tem o ano
from datetime import date 
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
    print(f'O ano {ano} tem 366 dias')
else:
    print(f'O ano {ano} é comum')
    print(f'O ano {ano} tem 365 dias')




