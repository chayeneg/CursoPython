"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = int(len(input('qual o seu nome: ')))

if nome <= 4:
    print('seu nome é curto')
elif nome >=5 and nome <=6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')