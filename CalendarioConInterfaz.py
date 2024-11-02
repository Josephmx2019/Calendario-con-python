import calendar
import tkinter as tk
from tkinter import messagebox

def mostrar_calendario_completo():
    year = int(entry_año.get())
    resultado.config(state=tk.NORMAL)
    resultado.delete(1.0, tk.END)
    for i in range(1, 13):
        resultado.insert(tk.END, calendar.month(year, i))
        resultado.insert(tk.END, '\n\n')
    resultado.config(state=tk.DISABLED)

def mostrar_calendario_personalizado():
    año = int(entry_año_personalizado.get())
    mes = var_mes.get()
    meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
    mes_numero = meses.get(mes)
    if mes_numero is not None:
        resultado.config(state=tk.NORMAL)
        resultado.delete(1.0, tk.END)
        resultado.insert(tk.END, calendar.month(año, mes_numero))
        resultado.insert(tk.END, '\n\n')
        resultado.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Error", "Mes no válido")

def salir_programa():
    respuesta = messagebox.askyesno("Salir", "¿Está seguro de que desea salir?")
    if respuesta:
        root.destroy()

root = tk.Tk()
root.title("Calendario")

# Calendario completo
frame_completo = tk.Frame(root)
frame_completo.pack(pady=10)

label_año = tk.Label(frame_completo, text="Año:")
label_año.grid(row=0, column=0, padx=10)

entry_año = tk.Entry(frame_completo)
entry_año.grid(row=0, column=1, padx=10)

btn_completo = tk.Button(frame_completo, text="Mostrar Calendario Completo", command=mostrar_calendario_completo)
btn_completo.grid(row=0, column=2, padx=10)

# Calendario personalizado
frame_personalizado = tk.Frame(root)
frame_personalizado.pack(pady=10)

label_año_personalizado = tk.Label(frame_personalizado, text="Año:")
label_año_personalizado.grid(row=0, column=0, padx=10)

entry_año_personalizado = tk.Entry(frame_personalizado)
entry_año_personalizado.grid(row=0, column=1, padx=10)

label_mes = tk.Label(frame_personalizado, text="Mes:")
label_mes.grid(row=0, column=2, padx=10)

var_mes = tk.StringVar()
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
var_mes.set(meses[0])

combo_mes = tk.OptionMenu(frame_personalizado, var_mes, *meses)
combo_mes.grid(row=0, column=3, padx=10)

btn_personalizado = tk.Button(frame_personalizado, text="Mostrar Calendario Personalizado", command=mostrar_calendario_personalizado)
btn_personalizado.grid(row=0, column=4, padx=10)

# Resultado
resultado = tk.Text(root, height=20, width=50, state=tk.DISABLED)
resultado.pack(pady=10)

# Botón salir
btn_salir = tk.Button(root, text="Salir", command=salir_programa)
btn_salir.pack()

root.mainloop()
