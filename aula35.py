"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
#Quando eu não quero que ele pegue o 0
contador = 0
while contador < 10:
    contador = contador + 1
    print(contador)
print("acabou")
#Quando eu quero que ele pegue o 0
contador = 0
while contador < 10:
    print(contador)
    contador = contador + 1
print("acabou")
