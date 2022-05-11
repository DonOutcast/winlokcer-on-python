from tkinter import *
from tkinter import messagebox
def btn_click():
    key = ent.get()
    if key == 'ПАРОЛЬ':
        messagebox.showinfo(title='Успех', message='Windows разблокирован.')
        root.destroy()
root = Tk()
root.title('Windows заблокирован!')
root.geometry('400x200')
Label(root, text='Введите пароль', font='Arial 25').pack()
ent = Entry(root, text='',font='Arial 25', width='15')
ent.pack()
Button(root, text='Разблокировать', font='Arial 25', command = btn_click).pack()
root.mainloop()
