def calculator():
    
    number1 = float(input('Digite o primeiro numero: '))
    number2 = float(input('Digite o primeiro numero: '))
    
    operation=(input('Qual a operação? '))
    
    if operation == '+':
        print(f'{number1} + {number2}=')
        print(number1 + number2)

    elif operation == '-':
        print(f'{number1} - {number2}')
        print(number1 - number2)

    elif operation == '*':
        print(f'{number1} * {number2}=')
        print(number1 * number2)
    
    elif operation == '/':
        print(f'{number1} / {number2}=')
        print(number1 / number2)
    
    else:
        print('Você não digitou um operador valido, rode o programa denovo')

    again()

def again():

    calc_again = input('Deseja rodar o programa dnv?')

    if calc_again.upper() == 'S':
        calculator()
    
    elif calc_again.upper() == 'N':
        print('Vejo você depois')
    
    else:
        again()

def welcome():
    print('Seja bem vindo a calculadora')

welcome()
calculator()