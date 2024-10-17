import json
from json import JSONDecodeError


class Tarea:
    # Creo un constructor de la clase tarea que se inicializa con una descripcion
    # y un booleano para indicar si esta completada
    def __init__(self,descripcion,completado = False):
        self.descripcion = descripcion
        self.completado = completado

    # Creamos un metodo para abrir el archivo, leerlo y convertirlo
    # a una lista de tareas, si no encuentra archivo devuelve una lista vacía
    # Usamos with open para que el archivo se cierre automáticamente
    def cargarTareasEnLista(archivo:str):
        try:
            with open(archivo,"r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Creamos un metodo para convertir una tarea a un formato de diccionaro para almacenarlo en el archivo JSON
    # En este caso descripcion y completada son claves dentro del diccionario, y self.descripcion y self.completado
    # son valores, un diccionario funciona con pares Clave-Valor
    #En vez de pasarle una tarea, ponemos self, y cuando pongamos nombreTarea.convertirTareaADiccionario
    #Y usemos el metodo, se convertira esa tarea a diccionario
    def convertirTareaADiccionario(self):
        return {"descripcion":self.descripcion,
                "completada": self.completado}

    # Para crear una tarea, le pasamos la lista de tareas y la descripción
    def crearTarea(tareas,descripcion):
        # Creamos un objeto tarea
        tarea = Tarea(descripcion)
        # Y lo añadimos a la lista con append,antes de añadirla hay que convertirla a formato diccionario
        tareas.append(tarea.convertirTareaADiccionario())

    # Creamos un metodo para listar todas las tareas
    def listarTareasSesion(tareas):
        #Usamos un bucle para recorrer todas las tareas, utilizamos enumerate
        # porque proporciona a la vez la clave y el valor
        for indice, tarea in enumerate(tareas):
            #Hacemos un if para no poner True o False en el estado de la tarea
            estado = "Completado" if tarea["completada"] else "No completada"
            print(f"{indice + 1}--> {tarea["descripcion"]} {estado}")


    # Despues de crear una tarea tenemos que guardarla en el archivo
    def guardarTareas(archivo: str, tareas):
        print("Lista de tareas existentes")
        #Antes de guardar directamente las tareas, nos las debemos descargar, añadir las nuevas
        # y luego volverlas a escribir todas en el archivo json
        datos = Tarea.listarTodasTareas(archivo) #Las guardamos en datos
        #Uso datos.extend para añadir la lista de tareas creadas en esta sesion, a todos los datos ya existentes
        datos.extend(tareas)
        # Abrimos el archivo en modo escritura w
        with open(archivo, "w") as file:
            # Y con el metodo json.dump escribimos todas las tareas de la lista y las escribe en el archivo
            # Importante que estén en formato diccionario para escribirlas en el archivo
            json.dump(datos, file, indent=4)
            print("Lista de tareas añadidas")
            for tarea in tareas:
                print(tarea)
        tareas.clear()

    def listarTodasTareas(archivo:str):
        try:
            with open(archivo, "r") as file:
                datos = json.load(file)
                #Recorremos los datos con un enumerate, ya que nos da clave y valor
            for indice, tarea in enumerate(datos):
                #Hacemos un if para no poner True o False en el print, e imprimimos el estado de cada tarea,
                #Si es True ponemos Completada y si es False, No completada
                estado = "Completada" if tarea["completada"] else "No completada"
                print(f"{indice + 1} --> {tarea['descripcion']} - {estado}")
            return datos
        except (FileNotFoundError,JSONDecodeError):
            datos = []
            return datos

    def borrarTareas(archivo:str,numero:int):
        #Hago un semaforo para ver si ha borrado algo o no
        semaforo:bool = False
        # Hacemos un contador que hará de índice
        contador = 1
        try:#Descargamos los archivos del json
            with open(archivo,"r") as file:
                datos = json.load(file)
                #Recorremos los archivos
            for tarea in datos:#Si nuestro contador coincide con
                # el numero que ha pasado el usuario entra en el if y borra la tarea, sale con un break
                if contador == numero:
                    datos.remove(tarea)
                    semaforo = True
                    break
                else:#Si no entra en el if sumamos 1 al contador
                    contador += 1
            #Si hemos borrado el archivo, ponemos un mensaje confirmandolo y si no, un mensaje de error
            print("Operación realizada con éxito") if semaforo else print("No se encontró esa tarea")
            #Una vez borrado un archivo, volvemos a subir los datos al json
            with open(archivo, "w") as file:
                json.dump(datos, file,indent=4)
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no se encontró.")
        except json.JSONDecodeError:
            print(f"Error: El contenido del archivo '{archivo}' no es un JSON válido.")

    def completarTarea(archivo:str,numero:int):
        #Hago un semaforo para ver si ha modificado algo o no
        semaforo:bool = False
        # Hacemos un contador que hará de índice
        contador = 1
        try:#Descargamos los archivos del json
            with open(archivo,"r") as file:
                datos = json.load(file)
                #Recorremos los archivos
            for tarea in datos:#Si nuestro contador coincide con
                # el numero que ha pasado el usuario entra en el if y cambiamos la tarea, sale con un break
                if contador == numero:
                    if not tarea['completada']:
                        tarea['completada'] = True
                        semaforo = True
                        break
                    else:
                        print("Esa tarea ya está completada")
                else:#Si no entra en el if sumamos 1 al contador
                    contador += 1
            #Si hemos borrado el archivo, ponemos un mensaje confirmandolo y si no, un mensaje de error
            print("Operación realizada con éxito") if semaforo else print("No se encontró esa tarea")
            #Una vez borrado un archivo, volvemos a subir los datos al json
            with open(archivo, "w") as file:
                json.dump(datos, file,indent=4)
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no se encontró.")
        except json.JSONDecodeError:
            print(f"Error: El contenido del archivo '{archivo}' no es un JSON válido.")