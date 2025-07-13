def somar (a, b):
    return a + b

def subtrair (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b == 0:
        return 'Erro: Divisão por zero!'
    return a / b

print('Calculadora em Python')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Divisão')

opcao = input('Escolha uma operação (1/2/3/4)')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))

if opcao == '1':
    print('Resultado: ', somar(n1, n2))

elif opcao == '2':
    print('Resultado: ', subtrair(n1, n2))

elif opcao == '2':
    print('Resultado: ', multiplicar(n1, n2))

elif opcao == '2':
    print('Resultado: ', dividir(n1, n2))

else:
    print('Opção Inválida')    
    