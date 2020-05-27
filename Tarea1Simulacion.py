from tkinter import *
from tkinter import messagebox
import random as rad

# Siempre que vayamos a usar tkinter, hay que usar root
# from tkinter import IntVar

root = Tk()
root.geometry("300x300+300+300")
root.title("Probabilidad de dados")

# Labels -----------
labelLad1 = Label(root, text="lado #1")
labelLad2 = Label(root, text="lado #2")
labelLad3 = Label(root, text="lado #3")
labelLad4 = Label(root, text="lado #4")
labelLad5 = Label(root, text="lado #5")
labelLad6 = Label(root, text="lado #6")

labelLad1.grid(row=0, column=0)
labelLad2.grid(row=1, column=0)
labelLad3.grid(row=2, column=0)
labelLad4.grid(row=3, column=0)
labelLad5.grid(row=4, column=0)
labelLad6.grid(row=5, column=0)
# End Label -------------

# Entries ------------

entryLad1 = Entry(root)
entryLad2 = Entry(root)
entryLad3 = Entry(root)
entryLad4 = Entry(root)
entryLad5 = Entry(root)
entryLad6 = Entry(root)
entryLad1.insert(END, 0)
entryLad2.insert(END, 0)
entryLad3.insert(END, 0)
entryLad4.insert(END, 0)
entryLad5.insert(END, 0)
entryLad6.insert(END, 0)

entryLad1.grid(row=0, column=1)
entryLad2.grid(row=1, column=1)
entryLad3.grid(row=2, column=1)
entryLad4.grid(row=3, column=1)
entryLad5.grid(row=4, column=1)
entryLad6.grid(row=5, column=1)
# End Entry -----------

# variable "variable" para cambiar el label del total

result = IntVar()

# Label para total de las probabilidades
totalLabel = Label(root, textvariable=result)
totalLabel.grid(row=6, column=1)


def Total():
    if len(entryLad1.get()) == 0 or len(entryLad2.get()) == 0 or len(entryLad3.get()) == 0 or len(entryLad4.get()) == 0 or len(entryLad5.get()) == 0 or len(entryLad6.get()) == 0:
        messagebox.showinfo("Error 404", "No puede tener campos vacios")
    else:
        value1 = float(entryLad1.get())
        value2 = float(entryLad2.get())
        value3 = float(entryLad3.get())
        value4 = float(entryLad4.get())
        value5 = float(entryLad5.get())
        value6 = float(entryLad6.get())
        result.set(value1 + value2 + value3 + value4 + value5 + value6)


# boton para total de probabilidades
myButton = Button(root, text="Calcular Total", command=Total, borderwidth=5)
myButton.grid(row=6, column=0)


diceSides = [1, 2, 3, 4, 5, 6]
outcome = IntVar()
outcomeLabel = Label(root, textvariable=outcome)
outcomeLabel.grid(row=8, column=1)


def Probability():
    if result.get() == 0:
        a = rad.choices(diceSides, weights=None, cum_weights=None, k=1)
        b = a[0]
        outcome.set(b)
    elif result.get() > 100:
        messagebox.showinfo("Error 404", "El total no puede ser mayor a 100")
    elif result.get() < 0:
        messagebox.showinfo("Error 404", "El total no puede ser menor a 0")
    else:
        a = rad.choices(diceSides, weights=[float(entryLad1.get()), float(entryLad2.get()), float(entryLad3.get()), float(entryLad4.get()), float(entryLad5.get()), float(entryLad6.get())], cum_weights=None, k=1)
        b = a[0]
        outcome.set(b)


calcuButton = Button(root, text="Tirar Dados", command=Probability)
calcuButton.grid(row=7, column=0)

diceLabel = Label(root, text="El lado que salio es: ")
diceLabel.grid(row=8, column=0)


root.mainloop()
