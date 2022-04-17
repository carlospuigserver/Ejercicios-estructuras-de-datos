class naturaleza:
    def __init__(self):
        self.alimentaria=0.055
        self.servicio=0.2

class producto(naturaleza):
    def __init__(self,TasaIva):
        self.TasaIva=TasaIva

def facturar(self):
    return 100+100*self.TasaIva

class factoryfactura(producto):
    def __init__(self):
        pass

def crear(self):
    clase=producto(self.TasaIva)
    return clase
