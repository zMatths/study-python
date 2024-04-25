primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor: {primeiro_valor} é MAIOR que o segundo valor: {segundo_valor}')

elif primeiro_valor == segundo_valor:
    print(f'O primeiro valor: {primeiro_valor} é IGUAL ao segundo valor: {segundo_valor}')

elif primeiro_valor < segundo_valor:
    print(f'O primeiro valor: {primeiro_valor} é MENOR ao segundo valor: {segundo_valor}')