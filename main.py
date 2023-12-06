# Interface simples

from conversor import cel_fah

while True:
    # Apresentação
    print('\n\t\t\t -- Conversor --\n')

    # Menu
    print('1. Converter ºC em ºF')
    print('2. Sair')

    # Ler a opção do usuário
    op = int(input('\nInforme a opção: '))

    if op == 1:
        # Entrada
        cel = float(input('Informe a temperatura em ºC: '))

        # Processamento
        fah = cel_fah(cel)

        # Saída
        print('\n{:.2f}ºC = {:.2f}ºF\n'.format(cel, fah))
    elif op == 2:
        print('\nForte abraço!\n')
        break
    else:
        print(f'Opção {op} incorreta!')
