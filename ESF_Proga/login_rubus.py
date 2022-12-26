import PySimpleGUI as sg
from SqlLite import *

layout = [[sg.Text('Введите логин:  '), sg.InputText(size=(30, 10), k='_login_')],
          [sg.Text('Введите пароль:'), sg.InputText(size=(30, 10), k='_password_', password_char='*')],
          [sg.Submit('Сохранить', k='_save_'), sg.Submit('Просмотр аккаунтов', k='_watch_'), sg.Cancel('Закрыть', k='_close_')],
          [sg.Text('Какой аккаунт удалить(Укажите номер аккаунта)')],
          [sg.InputText(size=(30, 10), k='_userid_'), sg.Submit('Удалить', k='_del_')],
          [sg.Output(size=(55, 10), k='_output_')],
          [sg.Submit('Очистить')]
          ]
window = sg.Window('Аккаунт Rubus', layout)

while True:
    event, values = window()
    if event in (sg.WINDOW_CLOSED, '_close_'):
        break
    if event == '_save_':
        window.perform_long_operation(lambda: get_add(values['_login_'], values['_password_']), '-FUNCTION COMPLETED-')
    if event == '_watch_':
        window.perform_long_operation(lambda: get_watch_db(), '-FUNCTION COMPLETED-')
    if event == '_del_':
        window.perform_long_operation(lambda: get_delete(values['_userid_']), '-FUNCTION COMPLETED-')
    if event == "Очистить":
        window.FindElement('_output_').Update('')

window.close()
