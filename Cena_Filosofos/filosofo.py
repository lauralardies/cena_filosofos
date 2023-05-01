import threading
import time

class Filosofo():
    def __init__(self, id, semaforos, gui):
        self.id = id
        self.semaforos = semaforos
        self.gui = gui
        self.tenedor_izq = id
        self.tenedor_der = (id + 1) % 5
        self.estado = 'Pensando'
        self.run_thread = threading.Thread(target=self.run, args=())

    def start(self):
        self.run_thread.start()

    def run(self):
        while True:
            # Pensando
            self.estado = 'Pensando'
            self.gui.update_filosofo(self.id, self.estado)
            time.sleep(2)
            # Esperando a tener los tenedores
            self.estado = 'Esperando'
            self.gui.update_filosofo(self.id, self.estado)
            self.semaforos[self.tenedor_izq].acquire()
            self.semaforos[self.tenedor_der].acquire()
            # Comiendo
            self.estado = 'Comiendo'
            self.gui.update_filosofo(self.id, self.estado)
            time.sleep(2)
            # Soltando los tenedores
            self.semaforos[self.tenedor_izq].release()
            self.semaforos[self.tenedor_der].release()