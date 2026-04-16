# calculadora.py
# Alterando o código para o commit e push

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

def exibir_menu():
    print("\n=== CALCULADORA ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "5":
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in {"1", "2", "3", "4"}:
            print("Opção inválida. Tente novamente.")
            continue

        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(num1, num2)
            elif opcao == "2":
                resultado = subtrair(num1, num2)
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
            elif opcao == "4":
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
