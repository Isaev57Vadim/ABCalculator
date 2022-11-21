# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()

# Сооздание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "A/B калькулятор", font = ('ALGERIAN', 15, 'bold'), fg = '#ff0011')
lblTitle.place(x=45, y=20)

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кн закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
