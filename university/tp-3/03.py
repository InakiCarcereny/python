FILE_PATH = r"D:\Users\Iñaki\Desktop\Dev\python\university\tp-3\files\datos.txt"

with open(FILE_PATH, "r") as archivo:
    print([linea.strip() for linea in archivo])