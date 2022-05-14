from tkinter import *
from tkinter import messagebox
def btn_click():
    key = ent.get()
    if key == 'ПАРОЛЬ':
        messagebox.showinfo(title='Успех', message='Windows разблокирован.')
        root.destroy()
    else:
        messagebox.showwarning("Ошибкаа", "Неправильный пароль.")
def exits():
    if ent.get() != "ПАРОЛЬ":
        messagebox.showwarning("Ошибка", "Непаравильный пароль")
root = Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.attributes('-toolwindow', True)
root.title('Windows заблокирован!')
root.geometry('420x230')
root.protocol("WM_DELETE_WINDOW", exits)
Label(root, text='Введите пароль', font='Arial 25').pack()
ent = Entry(root, text='', font='Arial 25', width=15, show='*')
ent.pack()
Button(root, text='Разблокировать', font='Arial 25', command=btn_click).pack()
root.mainloop()
