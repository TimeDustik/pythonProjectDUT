import tkinter as tk


def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=30, font=('Arial', 30), justify='left', relief='sunken', bd=3, insertborderwidth=3)

entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), (' ', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=23, height=5, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text='C', width=48, height=5, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

equal_button = tk.Button(root, text='=', width=47, height=5, command=calculate)
equal_button.grid(row=5, column=2, columnspan=3)

root.mainloop()