primeiro_valor = input("Digite um valor:")
segundo_valor = input("Digite segundo valor:")

if primeiro_valor > segundo_valor:
    print("Primeiro valor",primeiro_valor,"é maior que o segundo valor",segundo_valor)
elif segundo_valor > primeiro_valor:
    print("Segundo valor",segundo_valor,"é maior que o segundo valor",primeiro_valor)
else:
    print("Nenhum é maior que outro")