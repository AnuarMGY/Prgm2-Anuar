vAxiomas = [
  "Entre tres puntos, solo pasa una lnea recta",
  "Una proposicion no puede ser verdadera y falsa al mismno tiempo",
  "Si dos numeros naturales tienen el mismo sucesor, esos dos numeros son el mismo numero",
  "Todas las rectas tienen una cantidad infinita de puntos",
  "Dos rectas paralelas nunca se tocan",
  "Dos lineas rectas nunca encierran algo"
]

class axiomaModel:
  def obtenerAxioma(self, vNumeroEscogido):
    vResultado = vAxiomas[vNumeroEscogido]
    return vResultado
