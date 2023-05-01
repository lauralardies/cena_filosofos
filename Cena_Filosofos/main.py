import tkinter as tk
from tkinter import ttk
from gui import GUI

def main():
    # Creamos la ventana principal
    root = tk.Tk()
    root.title('Cena de los Filósofos')
    root.geometry('800x600')

    # Creamos la GUI
    gui = GUI(root, 5)

    # Cambiamos el color de fondo
    root.configure(bg='AntiqueWhite1')

    style = ttk.Style()
    style.configure('TButton', borderwidth=0, borderradius=8, padding=6, font=('Constantia', 10))

    # Botón iniciar 
    boton_iniciar = ttk.Button(root, text='Iniciar', style='TButton', command=gui.start)
    boton_iniciar.place(x=50, y=550)

    # Botón salir
    boton_salir = ttk.Button(root, text='Salir', style='TButton', command=gui.salir)
    boton_salir.place(x=150, y=550)

    # Iniciamos el bucle principal de la ventana
    root.mainloop()