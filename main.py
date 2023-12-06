# Interface simples

from conversor import cel_fah


# Apresentação
print('\n\t\t\t -- Conversor --\n')

# Entrada
cel = float(input('Informe a temperatura em ºC: '))

# Processamento
fah = cel_fah(cel)

# Saída
print('\n{:.2f}ºC = {:.2f}ºF\n'.format(cel, fah))