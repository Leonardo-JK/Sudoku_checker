import math
from operator import indexOf
from os import strerror

class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    pass
    # Escribe tu código aquí.


class FileEmpty(StudentsDataException):
    pass
    # Escribe tu código aquí.


def check(mat):
    print("checking")
    for i in range(9):
        for j in range(9):
            
            for c in range(9):
                if c == j:
                    continue
                else:
                    if mat[i][j] == mat[i][c]:
                        r = "(" + str(i) + ", " + str(j) + ") igual a (" + str(i) + ", " + str(c) + ") - Col: " + str(i * 9 + j + 1) + " - " + str(i * 9 + c + 1)
                        return [False, r]
                    
            for r in range(9):
                if r == i:
                    continue
                else:
                    if mat[i][j] == mat[r][j]:
                        r = "(" + str(i) + ", " + str(j) + ") igual a (" + str(r) + ", " + str(j) + ") - Col: " + str(i * 9 + j + 1) + " - " + str(r * 9 + j + 1)
                        return [False, r]
                        
            x = math.ceil((i + 1) / 3) - 1              
            y = math.ceil((j + 1) / 3) - 1

            for k in range(3):
                for l in range(3):
                    if (x * 3) + k == i and (y * 3) + l == j:
                        continue
                    else:
                        if mat[i][j] == mat[(x * 3) + k][(y * 3) + l]:
                            r = "(" + str(i) + ", " + str(j) + ") igual a (" + str((x * 3) + k) + ", " + str((y * 3) + l) + ") - Col: " + str(i * 9 + j + 1) + " - " + str(((x * 3) + k) * 9 + ((y * 3) + l) + 1)
                            return [False, r]
    
    return [True,""]    
                

try:    
    try:
        fileOpen = open("plantillas.txt", "rt")

    except IOError as err:
        print("Error al leer el archivo.", strerror(err.errno))
    
    l = 1
    
    for line in fileOpen:
        mb = []
        index = 0
        if line[0] != '\n':
            for i in range(9):
                row = []
                
                for j in range(9):
                    row.append(line[index])
                    index = index + 1
                
                mb.append(row)
            
            resp = check(mb)
                            
            if resp[0]:
                print('Linea ', l, ' correcta.')
            else:
                print('Linea ', l, ', INCORRECTA.', resp[1])
        else:
            print("----")        
            
        l = l + 1
        
except WrongLine as wl:
    print("Error en los datos.")
except FileEmpty as fe:
    print("Archivo vacio.")
except StudentsDataException as sdr:
    print("Datos inexistentes.")
except:    
    print("Error")