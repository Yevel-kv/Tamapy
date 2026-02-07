#!/usr/bin/env python3

class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 40
        self.energia = 80
        self.vivo = True
        self.enfermo = False
        self.desmayado = False

    def actualizar(self):
        if not self.vivo:
            return
        self.hambre += 5
        self.energia -= 5
        if self.hambre > 70:
            self.energia -= 5
        if self.hambre > 85 and not self.enfermo:
            self.enfermo = True
            print(f'{self.nombre} se ha enfermado por hambre.')
        if self.energia <= 0 and not self.desmayado:
            self.desmayado = True
            print(f'{self.nombre} se ha desmayado por agotamiento.')
        if self.hambre >= 100:
            self.vivo = False
            print(f'{self.nombre} ha muerto por hambre.')
    
    def comer(self, comida):
        if not self.vivo:
            print(f'{self.nombre} no puede comer... esta muerto.')
            return
        self.hambre = max(0, self.hambre - comida.valor)
        print(f'{self.nombre} ha comido {comida.nombre} (-{comida.valor} hambre).')
        if self.hambre == 0:
            print(f'{self.nombre} está completamente satisfecho.')
        if self.enfermo and self.hambre < 50:
            self.enfermo = False
            print(f'{self.nombre} se ha recuperado de la enfermedad gracias a la comida.')


    def dormir(self, horas):
        if not self.vivo:
            return

        self.energia = min(100, self.energia + horas * 10)
        print(f"{self.nombre} durmió {horas} horas (+{horas*10} energía)")

        if self.desmayado and self.energia > 20:
            self.desmayado = False
            print(f"{self.nombre} despertó del desmayo.")

    def jugar(self):
        if not self.vivo:
            return

        if self.desmayado:
            print(f"{self.nombre} está desmayado y no puede jugar.")
            return

        if self.energia < 20:
            print(f"{self.nombre} está demasiado cansado para jugar.")
            return

        self.energia -= 15
        self.hambre += 10
        print(f"{self.nombre} jugó 🎾 (-15 energía, +10 hambre)")

    def estado(self):
        print(f"\n🐾 {self.nombre}")
        print(f"Hambre: {self.hambre}/100")
        print(f"Energía: {self.energia}/100")
        print(f"Enfermo: {'Sí' if self.enfermo else 'No'}")
        print(f"Desmayado: {'Sí' if self.desmayado else 'No'}")
        


class Comida:
    def __init__(self, nombre, valor_nutritivo):
        self.nombre = nombre
        self.valor = valor_nutritivo
    def descripcion(self):
        return f'Comida: {self.nombre}, Valor Nutritivo: {self.valor}'

class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascota = None       

    def alimentar_mascota(self, comida):
        for i in Comidas:
            if i.nombre == comida.nombre:
                if self.mascota:
                    self.mascota.comer(i)
                    print(f'{self.nombre} ha alimentado a {self.mascota.nombre} con {i.descripcion()}.')
                else:
                    print(f'{self.nombre} no tiene una mascota para alimentar.')
                return
    def hacer_dormir_mascota(self, horas):
        if self.mascota:
            self.mascota.dormir(horas)
            print(f'{self.nombre} ha hecho dormir a {self.mascota.nombre} por {horas} horas.')
        else:
            print(f'{self.nombre} no tiene una mascota para hacer dormir.')

    def mostrar_estado_mascota(self):
        if self.mascota:
            self.mascota.estado()
        else:
            print(f'{self.nombre} no tiene una mascota para mostrar su estado.')

class Juego:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []
        self.tiendas = []
        self.mascotas = []
        self.turno = 0
    
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    
    def agregar_tienda(self, tienda):
        self.tiendas.append(tienda)
    
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_menu(self):
        print("\n¿Qué quieres hacer?")
        print("1. Dar comida")
        print("2. Hacer dormir")
        print("3. Jugar")
        print("4. Ver estado")
        print("5. Pasar turno")
        print("6. Salir")

    def iniciar(self):
        mascota = self.mascotas[0]

        while mascota.vivo:
            self.mostrar_menu()
            opcion = input("> ")

            if opcion == "1":
                print("1. Croquetas  2. Pollito  3. Galleta")
                comida = input("> ")

                if comida == "1":
                    mascota.comer(Comidas[0])
                elif comida == "2":
                    mascota.comer(Comidas[1])
                elif comida == "3":
                    mascota.comer(Comidas[2])

            elif opcion == "2":
                horas = int(input("¿Cuántas horas? "))
                mascota.dormir(horas)

            elif opcion == "3":
                mascota.jugar()

            elif opcion == "4":
                mascota.estado()

            elif opcion == "5":
                self.avanzar_turno()

            elif opcion == "6":
                print("Saliendo del juego...")
                break

        print("\n💀 Juego terminado.")
    
    def actualizar(self):
        self.hambre += 5
        self.energia -= 5
        if self.hambre > 70:
            self.energia -= 5
        if self.hambre > 85 and not self.enfermo:
            self.enfermo = True
            print(f'{self.nombre} se ha enfermado por hambre.')
        if self.energia <= 0:
            self.desmayado = True
            print(f'{self.nombre} se ha desmayado por falta de energía.')
        if self.hambre >= 100:
            self.vivo = False
            print(f'{self.nombre} ha muerto por hambre.')

    def avanzar_turno(self):
        self.turno += 1
        print(f"\n Turno {self.turno}")
        for mascota in self.mascotas:
            if not mascota.vivo:
                print(f'{mascota.nombre} ha muerto y no puede continuar.')
            mascota.actualizar()


#Firulais = Mascota("Firulais", "Perro")
#Sophya = Dueño("Sophya")
#Sophya.mascota = Firulais
Comidas = [Comida("Croquetas", 20), Comida("Pollito", 30), Comida("Galleta", 10)]
#Sophya.alimentar_mascota(Comidas[1])
#Sophya.mostrar_estado_mascota()
#Sophya.hacer_dormir_mascota(1)
#Sophya.mostrar_estado_mascota()
#Sophya.mascota.jugar()
#Sophya.mostrar_estado_mascota()
juego = Juego("Tamapy")
juego.agregar_mascota(Mascota("Firulais", "Perro"))
juego.iniciar()
    