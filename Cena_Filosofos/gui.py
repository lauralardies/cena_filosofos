import math
import threading
import tkinter as tk
from filosofo import Filosofo

class GUI():
    def __init__(self, root, num_filosofos):
        self.root = root
        self.num_filosofos = num_filosofos
        self.filosofos = []
        self.botones = []
        self.semaforos = []
        self.colors = {'Pensando': 'SlateBlue2', 'Comiendo': 'sea green', 'Esperando': 'medium orchid'}
        
        # Configuramos caja de texto
        self.text = tk.Text(root, height=10, width=30)
        self.text.place(x=500, y=350)
        self.text.config(bg='AntiqueWhite1', font=('Constantia', 10))

        # Configuramos la geometría de la mesa redonda
        centro_x = 200
        centro_y = 250
        radio = 200
        angulo_inicial = -90
        angulo_por_filosofo = 360 // num_filosofos

        # Creamos cada filósofo y lo colocamos en la mesa redonda
        for i in range(num_filosofos):
            angulo = angulo_inicial + angulo_por_filosofo * i
            x = centro_x + int(radio * 0.8 * -1 * math.sin(math.radians(angulo)))
            y = centro_y + int(radio * 0.8 * math.cos(math.radians(angulo)))
            self.filosofos.append(Filosofo(i, self.semaforos, self))
            self.botones.append(tk.Button(root, text=f'Filosofo {i+1}', bg='white', width=15, font=('Constantia', 10)))
            self.botones[i].place(x=x, y=y)
            self.semaforos.append(threading.Semaphore(1))
            
        # Creamos la leyenda
        legend_frame = tk.Frame(root)
        legend_frame.configure(bg='AntiqueWhite1')
        legend_frame.place(x=600, y=50)
        for i, (estado, color) in enumerate(self.colors.items()):
            legend_cell = tk.Frame(legend_frame, width=15, height=15, bg=color)
            legend_cell.grid(row=i, column=0, padx=10, pady=10)
            legend_label = tk.Label(legend_frame, text=estado, font=('Constantia', 10))
            legend_label.configure(bg='AntiqueWhite1')
            legend_label.grid(row=i, column=1, padx=10)

    def start(self):
        for f in self.filosofos:
            f.start()

    def update_filosofo(self, id, estado):
        color = 'yellow'
        if estado == 'Pensando':
            color = 'SlateBlue2'
        elif estado == 'Comiendo':
            color = 'sea green'
        elif estado == 'Esperando':
            color = 'medium orchid'
        self.botones[id].config(bg=color)
        self.text.insert(tk.END, f'Filósofo {id+1} está {estado.lower()}.\n') # Cada acción va actualizando la caja de texto

    def salir(self):
        self.root.destroy()