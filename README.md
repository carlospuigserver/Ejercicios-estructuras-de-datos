# Ejercicios-estructuras-de-datos

El link de este repositorio es : https://github.com/carlospuigserver/Ejercicios-estructuras-de-datos.git

* He realizado esta tarea de ejercicios de estructuras de datos mediante la programación orientada a objetos

## Ejercicio 1
* Aquí hay clases que representan los elementos de sintaxis de un lenguaje de programación junto a un pequeño "programa" escrito usando estas clases. Escriba un visitante que pueda recorrer este programa y convertirlo en un programa de Python.

```
class Bloque: 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 


mostrar_ok = Mostrar('"OK"') 
mostrar_ko = Mostrar('"KO"') 
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
bloque_alternativa = Bloque() 
bloque_alternativa.agregarInstruction(alternativa) 
bucle = MientrasQue(True, bloque_alternativa) 
```

## Ejercicio 2
* Siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar, las convierta a mayúsculas y las escriba en un archivo. Tenga en cuenta que para beneficiarse plenamente de las ventajas del design pattern MVC, los atributos, en particular los del modelo, se deben encapsular.

```
from asyncore import write


class usuario:
    def __init__(self,linea1,linea2):
        self.linea1=linea1
        self.linea2=linea2
        #mayúsculas
        linea1.upper()
        linea2.upper()

def fichero(self):
    archivo=open("xxxx.txt","w")
    archivo.write(self.linea1)
    archivo.write(self.linea2)
    archivo.close()
    
```

## Ejercicio 3
*  Implementar un programa que factura productos por valor de 100, con la tasa de IVA correcta, según sean productos de alimentación o servicios.

```
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
```
