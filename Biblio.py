#!/usr/bin/env python3

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" no está disponible para préstamo.')

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print(f'El libro "{self.titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" no estaba prestado.')
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'El libro "{libro.titulo}" ha sido agregado a la biblioteca.')

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f'- {libro.titulo} por {libro.autor} [{estado}]')

    def prestar_libro(self, titulo, usuario):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.prestar()
                usuario.libros_prestados.append(libro)
                print(f'El libro {usuario.nombre} ha tomado "{libro.titulo}".')
                return
        print(f'El libro "{titulo}" no está disponible para préstamo o no existe en la biblioteca.') 
        if libro in usuario.libros_prestados:
            print(f'{usuario.nombre} ya tiene ese libro.')
            return           
    
    def devolver_libro(self, titulo, usuario):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                libro.devolver()
                usuario.libros_prestados.remove(libro)
                print(f'{usuario.nombre} ha devuelto el libro "{libro.titulo}".')
                return
        print(f'{usuario.nombre} no tiene el libro "{titulo}" prestado.')


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
    
    def mostrar_libros_prestados(self):
        print(f'Libros prestados por {self.nombre}:')
        for libro in self.libros_prestados:
            print(f'- {libro.titulo} por {libro.autor}')


biblio = Biblioteca()
biblio.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
biblio.agregar_libro(Libro("1984", "George Orwell"))
biblio.agregar_libro(Libro("Don Quijote de la Mancha", "Miguel de Cervantes"))
biblio.agregar_libro(Libro("El Principito", "Antoine de Saint-Exupéry"))
biblio.agregar_libro(Libro("La Sombra del Viento", "Carlos Ruiz Zafón"))
biblio.mostrar_libros()
ana = Usuario("Ana")
biblio.prestar_libro("Cien Años de Soledad", ana)
ana.mostrar_libros_prestados()