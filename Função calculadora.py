
def calculadora():
  while True:
    # Exibe o menu de opções
    print("** Calculadora **")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    # Pede a opção do usuário
    operacao = int(input("Digite o número da operação: "))

    # Valida a opção
    if operacao not in range(5):
      print("Essa opção não existe!")
      continue

    # Se for a opção de sair, termina o programa
    if operacao == 0:
      break

    # Pede os valores do usuário
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    # Executa a operação
    resultado = None
    if operacao == 1:
      resultado = valor1 + valor2
    elif operacao == 2:
      resultado = valor1 - valor2
    elif operacao == 3:
      resultado = valor1 * valor2
    elif operacao == 4:
      resultado = valor1 / valor2

    # Mostra o resultado
    print(f"Resultado: {resultado}")

# Executa a função calculadora
calculadora()
