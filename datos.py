import json

horario = []

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]



horas = [
    "06:00",
    "07:00",
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00"
]

try:
    with open("horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)
except FileNotFoundError:
    horario = []

def guardar_horario():
    with open("horario.json", "w", encoding="utf-8") as archivo:
              json.dump(horario, archivo, ensure_ascii=False, indent=4)


