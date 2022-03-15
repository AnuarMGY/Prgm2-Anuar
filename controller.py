import modelo
import vista

class axiomaTerminalController:
    def __init__(self):
        self.model = modelo.axiomaModel()
        self.view = vista.vistaAxiomasPorTerminal()
        self.view = vista.vistaAxiomasHTML()

    def run(self):
        while True:
          vNroDeAxiomaEscogido = int(self.view.escojerAxioma())
          if vNroDeAxiomaEscogido >= 1 and vNroDeAxiomaEscogido <= 6:
            break        
        vAxioma = self.model.obtenerAxioma(vNroDeAxiomaEscogido - 1)
        self.view.mostrar(vAxioma)