"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2:
        print("Número ímpar")
    else:
        print("Número par")
except ValueError:
    print("Informe um número inteiro válido")
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = int(input("Insira o horário (0-23): "))
    if hora >= 0 and hora <=11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print("Hora inválida")
except ValueError:
    print("Insira um dado que seja correspondente a hora")
    
 
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input("Digite seu nome :")
if len(nome) <= 4:
    print("seu nome é curto")
elif len(nome) >= 4 and len(nome) <= 6:
    print("Seu nome é normal")
elif len(nome) > 6:
    print("Seu nome é muito grande")
else:
    print("Insira um nome")
