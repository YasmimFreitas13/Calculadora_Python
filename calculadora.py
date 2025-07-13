while True:
    print("\n=== Calculadora ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = input("Escolha a operação (1/2/3/4 ou 0 para sair): ")

    if opcao == '0':
        print("Saindo da calculadora. Até mais!")
        break

    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = num1 + num2
    elif opcao == '2':
        resultado = num1 - num2
    elif opcao == '3':
        resultado = num1 * num2
    elif opcao == '4':
        if num2 == 0:
            print("Erro: divisão por zero!")
            continue
        resultado = num1 / num2

    print("Resultado:", resultado)
 
    