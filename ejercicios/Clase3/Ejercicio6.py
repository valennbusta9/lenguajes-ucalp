import builtins

# 1️⃣ Guardamos la función original
original_print = builtins.print

# 2️⃣ Definimos una nueva versión personalizada de print
def mi_print(*args, **kwargs):
    original_print("🧠 [Mensaje interceptado]:", *args, **kwargs)

# 3️⃣ Sobrescribimos la función print globalmente
builtins.print = mi_print

# 4️⃣ Ahora cualquier print usará la versión modificada
print("Hola mundo")
print("Esto está siendo interceptado")

# 5️⃣ Restauramos la función original
builtins.print = original_print

# 6️⃣ Ya vuelve a comportarse como antes
print("Print restaurado correctamente ✅")
