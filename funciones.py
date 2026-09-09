from datetime import datetime
import json

from datos import horario, guardar_horario, dias, horas

#FUNCION PARA GENERAR REPORTES

def construir_reporte():
    reporte = []

    for dia in dias:
        eventos_dia = []

        for evento in horario:
            if evento["dia"].lower() == dia.lower():
                eventos_dia.append({ 

                    "materia": evento["materia"],
                    "hora_inicio": evento["hora_inicio"],
                    "hora_fin": evento["hora_fin"],
                    "ubicacion": evento["ubicacion"]
                })

        if eventos_dia:
            reporte.append({
                "dia": dia,
                "eventos": eventos_dia
            })
    with open("reporte_horario.json", "w", encoding="utf-8") as archivo:
        json.dump(reporte, archivo, ensure_ascii=False, indent=4)

    return reporte

#FUNCION OPCION 1 - REGISTRAR MATERIA O ACTIVIDAD

def registrar_materia():
        materia = input("Ingrese el nombre de la materia o actividad: ")
        while True:
           dia = input("Ingrese el día de la semana: ")

           if dia.lower() in [d.lower() for d in dias]:
            break
           print("Día no valido, Debe ingresar un día de lunes a viernes.")
        while True:
           hora_inicio = input("Ingrese la hora de inicio (Formato 24 horas): ")
           hora_fin = input("Ingrese la hora de finalización (Formato 24 horas): ")

           if hora_inicio not in horas or hora_fin not in horas:
               print("Las horas deben estar entre las 6:00 y 18:00")
               continue

           inicio_nuevo = datetime.strptime(hora_inicio, "%H:%M")
           fin_nuevo = datetime.strptime(hora_fin, "%H:%M")

           if fin_nuevo <= inicio_nuevo:
               print("La hora de finalización debe ser posterior a la hora de inicio")
               continue
           
           
           break 
        
        ubicacion = input("Ingrese la ubicación: ")

        evento = {
            "materia": materia,
            "dia": dia,
            "hora_inicio": hora_inicio,
            "hora_fin": hora_fin,
            "ubicacion": ubicacion

        }
       
        conflicto = False

        for evento_existente in horario:
            if evento_existente["dia"].lower() == dia.lower():
                inicio_existente = datetime.strptime(
                    evento_existente["hora_inicio"], "%H:%M"
                )
                fin_existente = datetime.strptime(
                    evento_existente["hora_fin"], "%H:%M"
                )

                if inicio_nuevo < fin_existente and fin_nuevo > inicio_existente:
                    conflicto = True
                    break

        if conflicto:
            print("No se puede registrar la materia porque existe un choque de horario.")
        else:
            horario.append(evento)
            guardar_horario()
            print("Materia registrada exitosamente.")

#FUNCION OPCION 2 - MOSTRAR HORARIO

def mostrar_horario(): 
        print("Hora / " + "/".join(dias))
        print("-" * 70)

        for hora in horas:
            fila = [hora]

            hora_actual = datetime.strptime(hora, "%H:%M")

            for dia in dias:
                actividad = ""

                for evento in horario:
                    if evento["dia"].lower() == dia.lower():
                        inicio = datetime.strptime(evento["hora_inicio"], "%H:%M")
                        fin = datetime.strptime(evento["hora_fin"], "%H:%M")

                        if inicio <= hora_actual < fin:
                            actividad = evento["materia"]
                            break

                fila.append(actividad)

            print(" / ".join(fila))


#FUNCION OPCION 3 - MODIFICAR MATERIA O ACTIVIDAD


def modificar_materia():
    materia_buscar = input("Ingrese el nombre de la materia o actividad a modificar: ")
    
    encontrado = False
    
    for evento in horario:
        if evento["materia"].lower() == materia_buscar.lower():
                    encontrado = True
    
                    print("Materia encontrada:")
                    print("Día:", evento["dia"])
                    print("Hora:", evento["hora_inicio"], "-", evento["hora_fin"])
                    print("Ubicación", evento["ubicacion"])
    
                    while True:
                        nuevo_dia = input("Ingrese el nuevo día de la semana: ")
    
                        if nuevo_dia.lower() in [d.lower() for d in dias]:
                           break
    
                        print("Día no válido. Debe ingresar un día de lunes a viernes.")
    
                    while True:
                        nueva_hora_inicio = input("Ingrese la nueva hora de inicio: ")
                        nueva_hora_fin = input("Ingrese la nueva hora de finalización: ")
    
                        if nueva_hora_inicio not in horas or nueva_hora_fin not in horas:
                            print("Las horas deben estar entre las 06:00 y 18:00.")
                            continue
    
                        inicio_nuevo=datetime.strptime(nueva_hora_inicio, "%H:%M")
                        fin_nuevo=datetime.strptime(nueva_hora_fin, "%H:%M")
    
                        if fin_nuevo <= inicio_nuevo:
                            print("La hora de finalización debe ser posterior a la hora de inicio.")
                            continue
    
                        break
                    nueva_ubicacion = input("Ingrese la nueva ubicación (ENTER para mantener la misma): ")
    
                    if nueva_ubicacion == "":
                        nueva_ubicacion = evento["ubicacion"]
    
    
                    conflicto = False
    
                    for otro_evento in horario:
                            if otro_evento == evento:
                                continue
    
                            if otro_evento["dia"].lower() == nuevo_dia.lower():
                                inicio_existente = datetime.strptime(otro_evento["hora_inicio"], "%H:%M")
                                fin_existente = datetime.strptime(otro_evento["hora_fin"], "%H:%M")
    
                                if inicio_nuevo < fin_existente and fin_nuevo > inicio_existente:
                                    conflicto = True
                                    break
    
                    if conflicto:
                            print("No se puede modificar la materia porque existe un cruce de horario.")
                    else:
                            evento["dia"] = nuevo_dia
                            evento["hora_inicio"] = nueva_hora_inicio
                            evento["hora_fin"] = nueva_hora_fin
                            evento["ubicacion"] = nueva_ubicacion
    
                            guardar_horario()
    
                            print("Materia modificada exitosamente!")
    
                            break
    
    if not encontrado:
                print("No se encontró la materia o actividad")

#FUNCION OPCION 4 - ELIMINAR MATERIA O ACTIVIDAD

def eliminar_materia():
    materia_eliminar = input("Ingrese el nombre de la materia o actividad que desea eliminar: ")
     
    while True:
                 dia_eliminar = input("Ingrese el día en el que está registrada: ")
                 if dia_eliminar.lower() in [d.lower() for d in dias]:
                  break
     
                 print("Día no válido. Debe ingresar un día de Lunes a Viernes.")
     
    encontrado = False
     
    for evento in horario:
                 if (evento["materia"].lower() == materia_eliminar.lower() and evento["dia"].lower() == dia_eliminar.lower()):
                     horario.remove(evento)
                     guardar_horario()
                     encontrado = True
                     print("Materia o actividad eliminada exitosamente!")
                     break
    if not encontrado:
                 print("No se encontró la materia o actividad en ese día.")

#FUNCION OPCION 5 - GENERAR REPORTE DEL HORARIO

def generar_reporte():
    reporte = construir_reporte()
     
    print("******************************************")
    print("REPORTE DEL HORARIO SEMANAL")
    print("******************************************")
     
    contador = 0
     
    for dia in reporte:
        print(dia["dia"] + ":")
     
        for evento in dia["eventos"]:
            print(
                "-",
                evento["materia"],
                f"({evento['hora_inicio']} - {evento['hora_fin']})",
                "en",
                evento["ubicacion"]
                 )
     
            contador += 1
     
            if contador == 5:
                input("Presione ENTER para continuar...")
                contador = 0
     
            print("******************************************")
     
            print("Reporte guardado en reporte_horario.json")

#FUNCION OPCION 6 - SALIR DEL PROGRAMA

def salir_programa():
        print("Gracias por utilizar el generador de horarios :).")
       
#FUNCION EXAMEN - BALANCE SALUDABLE

def balance_saludable():
    try:
        with open("horario.json", "r", encoding="utf-8") as archivo: horario_json = json.load(archivo)
    except FileNotFoundError:
          print ("No se encontró el archivo Json")
          return

reporte = []

for dia in dias:
        reporte_dia = []

        for evento in horario:
            if evento["dia"].lower() == dia.lower():
                reporte_dia.append({ 

                    "horas": evento["materia"],
                    "clases": evento["hora_inicio"],
                    "estudio": evento["hora_fin"],
                    "descanso": evento["ubicacion"]
                })
    
if total == 0:
     print("No existen materias registradas")
     

print("\nRESUMEN SEMANAL")
print(f"Total de materias en la semana: {total}")

for dia in dias:
         if cantidad_dia == 0:

           for evento in horario:
                if evento["dia"].lower == dia.lower():
                     cantidad_dia = +1

print(f"{"dia"}: {cantidad_dia} actividades")

with open("reporte_balance.json", "w", encoding="utf-8") as archivo:
                  json.dump(horario, archivo, ensure_ascii=False, indent=4)

         

          

              

              
