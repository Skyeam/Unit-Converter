#█   █ █   █ ███ █████     ███   ███  █   █ █   █ █████ █   █ █████ █████ ████
#█   █ ██  █  █    █      █     █   █ ██  █ █   █ █     ██  █   █   █     █   █
#█   █ █ █ █  █    █      █     █   █ █ █ █ █   █ ████  █ █ █   █   ████  ████
#█   █ █  ██  █    █      █     █   █ █  ██  █ █  █     █  ██   █   █     █  █
# ███  █   █ ███   █       ███   ███  █   █   █   █████ █   █   █   █████ █   █
import tkinter as tk
from tkinter import ttk
przeliczniki = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}
przeliczniki_wagi = {
    "milligram": 0.000001,
    "gram": 0.001,
    "kilogram": 1,
    "ounce": 0.0283495,
    "pound": 0.453592
}
unit1 = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
unit2 = ["milligram", "gram", "kilogram", "ounce", "pound"]
unit3 = ["Celsius", "Fahrenheit", "Kelvin"]
wynik = 0
wynik2 = 0
wynik3 = 0
def main():
    global unit1, unit2, unit3, listbox1, listbox2, value1, value2, listbox1_w, listbox2_w, listbox1_t, listbox2_t, value1_w, value2_w, value1_t, value2_t

    root = tk.Tk()
    root.title("Unit Conventer")
    root.geometry("500x500")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    tab_length = tk.Frame(notebook)
    tab_weight = tk.Frame(notebook)
    tab_temperature = tk.Frame(notebook)

    notebook.add(tab_length, text="Length")
    notebook.add(tab_weight, text="Weight")
    notebook.add(tab_temperature, text="Temperature")

    # ---------- Length ----------
    value1 = tk.Entry(tab_length)
    value2 = tk.Label(tab_length, text="Unit Conventer")
    value1.place(x=170, y=70)
    value2.place(x=170, y=20)

    listbox1 = tk.Listbox(tab_length, height=8, exportselection=False)
    for i in unit1:
        listbox1.insert(tk.END, i)

    listbox2 = tk.Listbox(tab_length, height=8, exportselection=False)
    for j in unit1:
        listbox2.insert(tk.END, j)

    listbox1.place(x=70, y=120)
    listbox2.place(x=300, y=120)

    sumbit = tk.Button(tab_length, text="Sumbit", command=sum1)
    sumbit.place(x=210, y=400)
    reset = tk.Button(tab_length, text="Reset", command=reset1)
    reset.place(x=210, y=445)
    # ---------- Weight ----------
    value1_w = tk.Entry(tab_weight)
    value2_w = tk.Label(tab_weight, text="Unit Conventer")
    value1_w.place(x=170, y=70)
    value2_w.place(x=170, y=20)

    listbox1_w = tk.Listbox(tab_weight, height=8, exportselection=False)
    for i in unit2:
        listbox1_w.insert(tk.END, i)

    listbox2_w = tk.Listbox(tab_weight, height=8, exportselection=False)
    for j in unit2:
        listbox2_w.insert(tk.END, j)

    listbox1_w.place(x=70, y=120)
    listbox2_w.place(x=300, y=120)

    sumbit_w = tk.Button(tab_weight, text="Sumbit", command=sum2)
    sumbit_w.place(x=210, y=400)
    reset_w = tk.Button(tab_weight, text="Reset", command=reset2)
    reset_w.place(x=210, y=445)
    # ---------- Temperature ----------
    value1_t = tk.Entry(tab_temperature)
    value2_t= tk.Label(tab_temperature, text="Unit Conventer")
    value1_t.place(x=170, y=70)
    value2_t.place(x=170, y=20)

    listbox1_t = tk.Listbox(tab_temperature, height=8, exportselection=False)
    for i in unit3:
        listbox1_t.insert(tk.END, i)

    listbox2_t = tk.Listbox(tab_temperature, height=8, exportselection=False)
    for j in unit3:
        listbox2_t.insert(tk.END, j)

    listbox1_t.place(x=70, y=120)
    listbox2_t.place(x=300, y=120)

    sumbit_t = tk.Button(tab_temperature, text="Sumbit", command=sum3)
    sumbit_t.place(x=210, y=400)
    reset_t = tk.Button(tab_temperature, text="Reset", command=reset3)
    reset_t.place(x=210, y=445)
    root.resizable(False, False)
    root.mainloop()
def sum1():
    checked_unit1 = listbox1.get(listbox1.curselection()[0])
    checked_unit2 = listbox2.get(listbox2.curselection()[0])
    try:
        wartosc = float(value1.get())
    except ValueError:
        value2.config(text="Enter the correct number!")
    wartosc_w_metrach = wartosc * przeliczniki[checked_unit1]
    wynik = wartosc_w_metrach / przeliczniki[checked_unit2]
    value2.config(text=f"Result: {wynik:.4f} {checked_unit2}")
def sum2():
    checked_unit1_w = listbox1_w.get(listbox1_w.curselection()[0])
    checked_unit2_w = listbox2_w.get(listbox2_w.curselection()[0])
    try:
        wartosc = float(value1_w.get())
    except ValueError:
        value2_w.config(text="Enter the correct number!")
    wartosc_w_kg = wartosc * przeliczniki_wagi[checked_unit1_w]
    wynik = wartosc_w_kg / przeliczniki_wagi[checked_unit2_w]
    value2_w.config(text=f"Result: {wynik:.4f} {checked_unit2_w}")
def to_celsius(wartosc, jednostka):
    if jednostka == "Celsius":
        return wartosc
    elif jednostka == "Fahrenheit":
        return (wartosc - 32) * 5/9
    elif jednostka == "Kelvin":
        return wartosc - 273.15
def from_celsius(wartosc_c, jednostka):
    if jednostka == "Celsius":
        return wartosc_c
    elif jednostka == "Fahrenheit":
        return wartosc_c * 9/5 + 32
    elif jednostka == "Kelvin":
        return wartosc_c + 273.15
def sum3():
    checked_unit1_t = listbox1_t.get(listbox1_t.curselection()[0])
    checked_unit2_t = listbox2_t.get(listbox2_t.curselection()[0])
    try:
        wartosc = float(value1_t.get())
    except ValueError:
        value2_t.config(text="Enter the correct number!")
    wartosc_w_celsius = to_celsius(wartosc, checked_unit1_t)
    wynik = from_celsius(wartosc_w_celsius, checked_unit2_t)

    value2_t.config(text=f"Result: {wynik:.2f} {checked_unit2_t}")
def reset1():
    value2.config(text="Unit Conventer")
    value1.delete(0, tk.END)
    listbox1.selection_clear(0, tk.END)
    listbox2.selection_clear(0, tk.END)
def reset2():
    value2_w.config(text="Unit Conventer")
    value1_w.delete(0, tk.END)
    listbox1_w.selection_clear(0, tk.END)
    listbox2_w.selection_clear(0, tk.END)
def reset3():
    value2_t.config(text="Unit Conventer")
    value1_t.delete(0, tk.END)
    listbox1_t.selection_clear(0, tk.END)
    listbox2_t.selection_clear(0, tk.END)
if __name__ == "__main__":
    main()

