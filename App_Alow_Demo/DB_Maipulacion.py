import sqlite3

conn = sqlite3.connect(r'C:\Users\alow.29\Documents\App\.venv1\Source\Data_Bases\usuarios.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM Usuarios;")

# Obtener todos los resultados
usuarios = cursor.fetchall()

# Imprimir cada fila
print("ID | Nombre | Contraseña | Tipo")
print("-------------------------------")
for i in range(len(usuarios)):
    print(usuarios[i])