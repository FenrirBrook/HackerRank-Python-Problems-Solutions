#Dados los nombres y calificaciones de cada estudiante en una clase de estudiantes, guárdelos en un archivo anidado.
# enumere e imprima los nombres de cualquier estudiante que tenga la segunda calificación más baja.
# Nota: Si hay varios estudiantes con la segunda calificación más baja, ordene su
# nombres en orden alfabético e imprima cada nombre en una nueva línea.
# Ejemplo
# La lista ordenada de puntuaciones es , por lo que la segunda puntuación más baja es .
# Hay dos alumnos con esa puntuación: . Ordenados alfabéticamente, los nombres se imprimen como:
# alfa
#beta 
# def run(ls):
#     u = []
#     for i in range(len(ls)): 
#         u.append(ls[i][1])

#     u = list(set(u))
#     u.sort()
#     ls = (sorted(ls, key=lambda x:x[0])) 
#     for i in range(len(ls)):
#         if ls[i][1] == u[1]:
#             print(ls[i][0])

# if __name__ == '__main__':
#     ls = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         ls.append([name, score])
#     run(ls)

def run(ls):
    u = []
    for i in range(len(ls)):
        u.append(ls[i][1])
    u = list(set(u))
    u.sort()
    ls = sorted(ls, key=lambda x:x[0])

    for i in range(len(ls)):
        if ls[i][1] == u[1]:
            print(ls[i][0])


if __name__ == '__main__':
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name, score])
    run(ls)

