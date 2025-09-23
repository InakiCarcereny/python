OUTPUT_PATH_NOTAS = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\alumnos.txt"
OUTPUT_PATH_INFO = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\info_alumnos.txt"
OUTPUT_PATH_PROMOCION = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-2\files\promocion.txt"

notas_alumnos = []
info_alumnos = []

def cargar_notas_alumno():
    seguir = True

    while seguir:
        legajo = input("Ingrese el legajo del estudiante: ")
        oral = int(input("Ingrese la nota del oral: "))
        escrito = int(input("Ingrese la nota del escrito: "))
        trabajos_practicos = int(input("Ingrese la nota del trabajo practico: "))

        notas_alumnos.append({
            "legajo": legajo,
            "oral": oral,
            "escrito": escrito,
            "trabajos practicos": trabajos_practicos
        })

        respuesta = input("Desea cargar otro usuario? (s) para si, (n) para no: ")

        if respuesta.lower() == "s":
            seguir = True
        else:
            seguir = False

    notas_alumnos.sort(key=lambda x: x["legajo"])

def cargar_info_alumno():
    for alumno in notas_alumnos:
        legajo = alumno["legajo"]
        nombre = input(f"Ingrese el nombre del alumno con numero de legajo {legajo}: ")
        apellido = input(f"Ingrese el apellido del alumno con numero de legajo {legajo}: ")

        info_alumnos.append({
            "legajo": legajo,
            "nombre": nombre,
            "apellido": apellido
        })

    info_alumnos.sort(key=lambda x: x["apellido"])

cargar_notas_alumno()

with open(OUTPUT_PATH_NOTAS, "w") as salida:
    for alumno in notas_alumnos:
        salida.write(f"{alumno["legajo"]};{alumno["oral"]};{alumno["escrito"]};{alumno["trabajos practicos"]} \n")

cargar_info_alumno()

with open(OUTPUT_PATH_INFO, "w") as salida:
    for alumno in info_alumnos:
        salida.write(f"{alumno["legajo"]};{alumno["nombre"]};{alumno["apellido"]} \n")

promocionados = []

for nota in notas_alumnos:
    promedio = (nota["oral"] + nota["escrito"] + nota["trabajos practicos"]) / 3
    if promedio >= 7:
        for alumno_info in info_alumnos:
            if alumno_info["legajo"] == nota["legajo"]:
                promocionados.append(alumno_info)

promocionados.sort(key=lambda x: x["apellido"])

with open(OUTPUT_PATH_PROMOCION, "w") as salida:
    for alumno in promocionados:
        salida.write(f'{alumno["apellido"]};{alumno["nombre"]} \n')
                    
    
            