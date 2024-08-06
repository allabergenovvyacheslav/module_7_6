import tkinter
from tkinter import Menu
from tkinter.messagebox import showinfo

window = tkinter.Tk()
window.title('Проводник')
window.geometry('353x220+300+300')
window.configure(bg='gray25')
window.resizable(False, False)


def info_wind():
    showinfo(title='Info', message='Инструкции работы окна Проводник:''\n'
                                   '1. нажмите на кнопку Выбор фала''\n'
                                   '2. откроется диск для выбора файлов''\n'
                                   '3. выберите файл')


def admin_wind():
    showinfo(title='Admin', message='Вячеслав Аллабергенов''\n'
                                    "Курс Python - разработчик"'\n'
                                    'Университет Urban')


main_menu = Menu(window)
window.config(menu=main_menu)

info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label='О программе', command='info_wind')

admin_menu = Menu(main_menu, tearoff=0)
admin_menu.add_command(label='Информация о разработчике', command='admin_wind')

main_menu.add_cascade(label='Info', menu=info_menu)
main_menu.add_cascade(label='Admin', menu=admin_menu)

window.mainloop()
