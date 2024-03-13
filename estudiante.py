class estudiantes:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.nota = notas

    def add_nota (self, notas):
        self.nota.append(notas)

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))

notas = []
numero_nota = int(input("¿Cuántas notas tiene el estudiante?: "))

for i in range(numero_nota):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

nueva_nota = float(input("Ingrese una nueva nota para el estudiante: "))
estudiantes = estudiantes(nombre, edad, notas)

estudiantes.add_nota(nueva_nota)



print("Datos del estudiante:")
print("Nombre:", estudiantes.nombre)
print("Edad:", estudiantes.edad)
print("Notas:", estudiantes.nota)
