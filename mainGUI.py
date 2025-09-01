# Interface gráfica do conversor de temperatura
import PySimpleGUI as psg

import conversor

frame_layout = [
    [psg.Radio('Celsius -> Fahrenheit', 'GRUPO2', default=True, key='cel_fah', enable_events=True)], # Erro3
    [psg.Radio('Fahrenheit -> Celsius', 'GRUPO1', key='cel_fah', enable_events=True)] # Erro4
]
layout = [
    [psg.Text('Informe a temperatura em ºC: ', key='rotulo'), psg.InputText(key='temp'), psg.Frame('Opções: ', layout=frame_layout)],
    [psg.Text('', key='resultado')],
    [psg.Button('Converter'), psg.Button('Limpar')],
]

janela = psg.Window('Conversor', layout)

while True:
    evento, valor = janela.read()

    if evento == psg.WIN_CLOSED or evento == 'Exit':
        break
    
    elif evento == 'cel_fah':
        janela['rotulo'].update('Informe a temperatura em ºC: ')
    
    elif evento == 'fah_cel':
        janela['rotulo'].update('Informe a temperatura em ºF: ')

    elif evento == 'Limpar':
        janela['temp'].update('')
        # Erro5
        janela['temp'].set_focus()
    else:
        if valor['cel_fah']:
            fah = conversor.cel_fah(float(valor['temp']))
            # Erro6
        else:
            # Erro7
            janela['resultado'].update('{:.2f} ºC'.format(cel))

        
janela.close()
