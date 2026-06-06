class Animal: 
    def __init__(self, nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def mostrar_información(self):
            print("Nombre:", self.nombre)
            print("Raza:", self.raza)
            print("Edad:", self.edad, "años")

            
    def hacer_sonido(self):
            print(self.nombre, "Esta haciendo un sonido")


mi_animal = Animal("Tobi","Perro","2")

     
mi_animal.mostrar_información()
mi_animal.hacer_sonido()
    