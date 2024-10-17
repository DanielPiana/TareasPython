from Tarea import Tarea
tareas =[]
archivo = "tareas.json"
while True:
    print("-----Menu-----"
          "\n1- Crear tarea"
          "\n2- Eliminar tarea"
          "\n3- Listar tareas"
          "\n4- Listar tareas sin guardar"
          "\n5- Guardar tareas creadas"
          "\n6- Completar una tarea"
          "\n0- Salir")

    opcion = input()
    match opcion:
        case "1":
            print("Escribe la descripción de la tarea")
            descripcion = input()
            Tarea.crearTarea(tareas,descripcion)
        case "2":
            print("Aqui tienes una lista de tareas! ¿Cual quieres borrar? Escribe su índice")
            Tarea.listarTodasTareas(archivo)
            numero = int(input())
            Tarea.borrarTareas(archivo,numero)
        case "3":
            print("Aqui tienes una lista de tareas!")
            Tarea.listarTodasTareas(archivo)
        case "4":
            print("Estas son las tareas creadas esta sesión")
            Tarea.listarTareasSesion(tareas)
        case "5":
            Tarea.guardarTareas(archivo, tareas)
        case "6":
            print("Aqui tienes una lista de tareas! ¿Cual quieres completar? Escribe su índice")
            Tarea.listarTodasTareas(archivo)
            numero = int(input())
            Tarea.completarTarea(archivo,numero)
        case "0":
            print("Adiós!!")
            break
        case _:
            print("Número no reconocido")
