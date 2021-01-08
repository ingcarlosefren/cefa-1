 
from UNIDAD6.MiRedS6_Listas import Principal
import UNIDAD6.S6Red

Principal()
"""
from UNIDAD6.Cuestionario6_1 import promedio_std

x=input("ingresa la lista de numeros")

print(promedio_std(x))

"""
"""
from UNIDAD6.Cuestionario6_1 import color_frecuente
lista=['rojo', 'rojo', 'azul', 'azul']
print(color_frecuente(lista))

"""
"""
#tablero = [[' ' , 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
          # 0   1   2   3   4   5   6  
tablero = [['X',' ',' ',' ',' ',' ',' '],#0
          [' ',' ',' ','X',' ','X',' '],#1
          [' ',' ',' ',' ','X',' ','X'],#2
          ['X',' ','X','X',' ',' ',' '],#3
          [' ',' ',' ',' ',' ',' ',' '],#4
          [' ','X',' ',' ',' ',' ',' '],#5
          ['X',' ',' ',' ','X',' ','X']]#6

def buscaminas(tablero, i, j):
  total_bom=0
  fila=i
  col=j
  for lista in tablero:
    tamaño_lista=len(lista)

  if i >=len(tablero) or j>=len(tablero):
    total_bom=total_bom
  else:
    for x in range(fila-1,fila+2):
      for y in range(col-1,col+2):
        if x>=0 and x<len(tablero) and y>=0 and y<tamaño_lista:
          if tablero[x][y]=="X":
            if x==fila and y==col:
              total_bom=total_bom
            else:
              total_bom=total_bom+1
        else:
          total_bom=total_bom
  
  return(total_bom)

print (buscaminas(tablero,3,2))
"""
"""
def buscaminas(tablero, i, j):
  for lista in tablero:
    tamaño_lista=len(lista)
    #print(type(tamaño_lista  ))

  total_bom=0
  fila=i
  col=j
  if i >=len(tablero) or j>=len(tablero):
    total_bom=total_bom
  else:
    for i in range(fila-1,fila+2):
      for j in range(col-1,col+2):
        if i>=0 and i<len(tablero) and j>=0 and j<tamaño_lista:
          if tablero[i][j]=="X":
            print("i,j: ",i,j)
            print("fila,col: ", fila, col)
            if i==fila and j==col:
              #cordenada1=str(i)+","+str(j)
              #print(cordenada1)
              print("true")
              total_bom=total_bom
              #print(total_bom)
            #else:
            # total_bom=0
            else:
              total_bom=total_bom+1
        else:
          #print("entro aqui")
          total_bom=total_bom
  
  return(total_bom)

print(buscaminas(tablero,3,3))
"""      

"""

from UNIDAD6.Cuestionario6_1 import buscaminas
tablero = [['X',' ',' ',' ',' ',' ',' '],#0
          [' ',' ',' ','X',' ','X',' '],#1
          [' ',' ',' ',' ','X',' ','X'],#2
          ['X',' ','X','X',' ',' ',' '],#3
          [' ',' ',' ',' ',' ',' ',' '],#4
          [' ','X',' ',' ',' ',' ',' '],#5
          ['X',' ',' ',' ','X',' ','X']]#6
#tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
#=[' ', 'X', 'M', 'X']


print(buscaminas(tablero,3,2))
#print(tablero2)
"""

#nombre=input("ingresa nombre: ")
#archivo_usuario = open("USERUNIDAD5/"+ nombre+".user","w")

#milista=list()

"""
texto="ingresa tu lista, separada por ',' "
milista=texto.split(",")
  
print(milista)
"""
"""
milista=["carlos", "david", "alba"]
milista.append("maria del mar")
milista.append("efren")
milista.append("milet")
milista.append("maria paz")
milista.extend(["carlos alonso","jesus"])
milista.insert(3,7000)

#for i in milista:
#print(milista)
milista.pop()
milista.remove("efren")

print(milista)
print( milista.index("milet"), "tamaño: ", len(milista))
nueva_lista=milista[0]
print(nueva_lista)
"""