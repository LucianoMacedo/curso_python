nome = input("Insira seu nome :")
idade = int(input("Insira sua idade :"))
if nome and idade:
    print(f'Seu nome é,{nome}')
    print(f'Seu nome invertido,{nome[::-1]}')
    if '' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f'seu nome tem,{len(nome)}')
    print(f'A primeira letra do seu nome é ,{nome[0]}')
    print(f'E a última letra é,{nome[-1]}')
    
else:
    print("Desculpe, você deixou campos vazios")