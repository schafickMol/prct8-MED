try:
    lectura = open("ejemplo3.txt")
except FileNotFoundError:
    print("El archivo -ejemplo3 3.txt -no Existe")