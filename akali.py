personaje = input("¿Quieres elegir a Gragas o Vladimir? ")

if personaje.lower() == "gragas":
    resultado = 0
    while True:
        resultado = 1 + resultado
        print(resultado)

elif personaje.lower() == "vladimir":
    resultado = 0
    while True:
        resultado = 2 + resultado
        print(resultado)

else:
    print("Ese personaje no está disponible. Por favor, elige entre Gragas o Vladimir.")