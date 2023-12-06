# Interface gráfica do conversor de temperatura
import PySimpleGUI as psg

import conversor

layout = [
    [psg.Text('Informe a temperatura em ºC: '), psg.InputText(key='cel')],
    [psg.Text('', key='fah')],
    [psg.Button('Converter'), psg.Button('Limpar')],
]

janela = psg.Window('Conversor', layout)

while True:
    evento, valor = janela.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['cel'].update('')
        janela['fah'].update('')
        janela['cel'].set_focus()
    else:
        fah = conversor.cel_fah(float(valor['cel']))
        janela['fah'].update('{:.2f} ºF'.format(fah))

janela.close()
