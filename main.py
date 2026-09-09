from funciones import generar_reporte, registrar_materia, mostrar_horario, modificar_materia, eliminar_materia, salir_programa, balance_saludable



def mostrar_menu():
    print("******************************************")
    print("GENERADOR DE HORARIOS PARA ESTUDIANTES")
    print("******************************************")
    print("1. Registrar una materia o actividad")
    print("2. Ver horario semanal")
    print("3. Modificar una materia o actividad")
    print("4. Eliminar una materia o actividad")
    print("5. Generar reporte del horario")
    print("6. Generar reporte de balance")
    print("7. Salir")
    print("******************************************")

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_materia()


    if opcion == "2": 
        mostrar_horario()

    if opcion == "3":
       modificar_materia()

    if opcion == "4":
       eliminar_materia()        


    if opcion == "5":
       generar_reporte()

    if opcion == "6":
        balance_saludable()

    if opcion == "7":
        salir_programa()
        break    