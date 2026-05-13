"""
crea una clase persona con los siguientes atributos: nombre , edad, género , y nacionalidad.
agrega un método para imprimir los datos de la persona y otro metodo para calcular el año
de nacimiento de la persona.
crea un objeto de la clase persona y utiliza los metodos para mostrar tu informacion y 
calcular su año de nacimiento.
"""
import detetime

class Personas:

    def __init__(self, nombre, edad, genero, nacionalidad = "Mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad

        def informacion(self):
            print("------Informacion------")
            print(f"{self.nombre}) ({self.genero})")
            print(f"Edad: {self.edad} años")
            print(f"Nacionalidad: {self.nacionalidad}")

        def calcularNacimiento(self):
            year = detetime 
 