class VistaGenerica():
  def mostrar(self, mensaje):
    return mensaje

  def escojerAxioma(self):
        vResultado = None
        vResultado = int(input("Tipee el numero de axioma que quiere ver: (1-6)"))
        return vResultado

class vistaAxiomasPorTerminal(VistaGenerica):
  def mostrar(self, mensaje):
    print("Y el axioma es: ", mensaje)

class vistaAxiomasHTML(VistaGenerica):
    def mostrar(self, mensaje):
        vArchivoHtml = open('vistaMVC.html', 'w')
        vPlantilla = """
        <html>
        <head>
        <title> Telematica - Prog2 </title>
        </head>
        <body> 
        <h1>Modelo-Vista-Controlador (MVC)</h1>
        <h2>Vista html</h2>
        <table border="1">
        <tbody>
        <tr>
        <td>y el Axioma es: </td>
        </tr>
        <tr>
        <td>        
        """
        vPlantilla += str(mensaje)
        vPlantilla += """
        </td>
        </tr>
        </tbody>
        </table>
        </body>
        </html>
        """

        vArchivoHtml.write(vPlantilla)
        vArchivoHtml.close()

#vt = vistaAxiomasHTML()
#vt.mostrar(vt.escojerAxioma())