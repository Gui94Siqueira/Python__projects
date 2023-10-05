    
print('           Bem vindo o que deseja fazer')
print('=-=' * 15)
def s (a, b):
    soma = a + b 
    print("soma: ", soma)
def sub (a, b):
    subtracao = a - b
    print("subtração: ", subtracao)
def div (a, b):
    divisao = a / b
    print("divisão: ", divisao)
def mult(a, b):
    multiplicacao = a * b
    print("multipicação: ", multiplicacao)
def lista ():
    print(''' 1* facilidade de aprendizado e utilização por diversos públicos;
2* versatilidade e uso para variados fins;
3* é uma linguagem gratuita e de fonte aberta;
4* pode ser usada em diversos sistemas operacionais;
5* grande número de bibliotecas, o que amplia as suas possibilidades.''')
    
opção = 0
while opção !=5:
    print('''    [1] Somar
    [2] Subtrair
    [3] Dividir
    [4] Multiplicar
    [5] Lista de vantagens em aprender python
    [6] Fim do programa. Volte sempre!''')
    opção = int(input("qual é a sua opção? "))
    if opção == 1:
        s(int(input('digite o primeiro numero: ')),int(input('digite o segundo numero: ')))
    elif opção == 2:
        sub (int(input('digite o primeiro numero: ')),int(input('digite o segundo numero: ')))
    elif opção ==3:
        div (int(input('digite o primeiro numero: ')),int(input('digite o segundo numero: ')))
    elif opção == 4:
        mult (int(input('digite o primeiro numero: ')),int(input('digite o segundo numero: ')))
    elif opção == 5:
        lista()
    elif opção >= 6:
        break
    
    print('=-=' * 15)
print('Fim do programa! Volte sempre!')
 
    
