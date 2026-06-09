import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        number = float(entry.get())

        square = number ** 2
        cube = number ** 3

        result_label.config(
            text=f"Квадраты: {square}\nКубы: {cube}"
        )

    except ValueError:
        messagebox.showerror("Қате", "Сан енгізіңіз!")



window = tk.Tk()
window.title("Квадрат және куб есептеу")
window.geometry("300x200")


label = tk.Label(window, text="Санды енгізіңіз:")
label.pack(pady=5)


entry = tk.Entry(window)
entry.pack(pady=5)


button = tk.Button(window, text="Есептеу", command=calculate)
button.pack(pady=10)


result_label = tk.Label(window, text="Нәтиже:")
result_label.pack(pady=10)


window.mainloop()



]asfgashf

