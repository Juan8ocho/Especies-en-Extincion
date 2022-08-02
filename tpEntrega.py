animales = []
cantidad = int(input("Indique la  cantidad de registros desea crear:"))
x = 0
while x <= cantidad:
    animal = input("Ingresa el nombre bulgar del animal: ")
    especie = input("Ingrese la especie: ")
    extincion = input("Indique si se encuentra en peligro de extinción: ")
    Población_Aproximada = input("Indique el numero de la población: ")
    nuevo_animal = {"Animal": animal, "Especie": especie,"Estado de extincion": extincion, "Tamaño de poblacion aproximado":Población_Aproximada}
    animales.append(nuevo_animal)
    x =x +1
for nuevo_animal in animales:
    if nuevo_animal["Estado de extincion"] == "si":
        print(nuevo_animal)



