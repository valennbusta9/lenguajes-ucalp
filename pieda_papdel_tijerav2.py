
import random

opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera (mejor de 5).")
print("Gana el primero que llegue a 3 victorias.\n")

puntos_usuario = 0
puntos_pc = 0
ronda = 1
rondas_totales = 5
objetivo = 3

while ronda <= rondas_totales and puntos_usuario < objetivo and puntos_pc < objetivo: #mientras no se llegue al limite de rondas y los puntos no lleguen al objetivo (3), sigo jugando

    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada (piedra/papel/tijera): ").strip().lower()

    # Valido la opcion
    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera. Intenta de nuevo.")
        continue  #si se ingresa un opcion no valida se vuelve a pedir y no cuenta como ronda

    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate. Se repite la ronda.")
        continue  #si hay empate no quiero que cuente la rondda

    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1

    print(f"Marcador: Tú {puntos_usuario} - {puntos_pc} PC")
    ronda += 1  #la ronda aumenta solamente su hay un ganador 

# Resultado final
print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
else:
    print("Perdiste, la computadora gana el juego 😢")
