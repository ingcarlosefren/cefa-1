"""
Pregunta 1
Escriba una función de nombre promedio_std(). La función debe recibir una lista de números llamada lista, y debe retornar retornar el promedio de ellos, junto con su desviación estándar.

Hint 1: La desviación estándar corresponde a la raíz de la suma de los cuadrados de las diferencias de cada elemento respecto al promedio, divididos por la cantidad de elementos.

Hint 2: Recuerda que puedes retonar dos valores x e y utilizando la notación
"""
def promedio_std(lista):
  n_lista=list()
  n_lista=lista
  print((lista))
  print((n_lista))
  suma=0
  varianza=0
  varianza2=0
  y=0
  for i in range (0,len(n_lista)):
    suma=suma+int(n_lista[i])
  x=suma/len(n_lista)
  for j in range (0, len(n_lista)):
    varianza=varianza+(int(n_lista[j])-x)**2

  varianza2=varianza/len(n_lista)
  y=varianza2**(1/2)

  return(x,y)

  """
Pregunta 2
Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: azul, rojo, verde y amarillo. Desea saber cual de esos colores es el que más se repite. Escriba una función color_frecuente que reciba como argumento a una lista de strings llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.

Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']

Debe retornar: "verde", 8

En caso de que haya varios colores con el máximo número, se retornará con la siguiente prioridad: azul, rojo, verde, amarillo. Es decir, por ejemplo si la lista es l = ['rojo', 'rojo', 'azul', azul'], la función debe retornar "azul", 2

  """
def color_frecuente(lista):
  colores=["azul","rojo","verde","amarillo"]
  azul=lista.count(str(colores[0]))
  rojo=lista.count(str(colores[1]))
  verde=lista.count(str(colores[2]))
  amarillo=lista.count(str(colores[3]))
  
  n_lista=[['azul',azul], ['rojo',rojo], ['verde',verde], ['amarillo', amarillo]]
  
  n_lista.sort(key=lambda color: color[1], reverse=True)
  Num_mayor=n_lista[0][1]
  i=0
  c_frecuente=""
  while i<len(n_lista):
    if str(n_lista[i][0])=="azul" and int(n_lista[i][1])==Num_mayor:
      c_frecuente=n_lista[i]
      i=len(n_lista)
    elif str(n_lista[i][0])=="rojo" and int(n_lista[i][1])==Num_mayor:
      c_frecuente=n_lista[i]
      i=len(n_lista)
    elif str(n_lista[i][0])=="verde" and int(n_lista[i][1])==Num_mayor:
      c_frecuente=n_lista[i]
      i=len(n_lista)
    elif str(n_lista[i][0])=="amarillo" and int(n_lista[i][1])==Num_mayor:
      c_frecuente=n_lista[i]
      i=len(n_lista)
    else:
      i=i+1


  return (c_frecuente)

"""
Pregunta 3
Un uso muy común de las listas es el de representar tableros con ellas. Para eso se utilizan listas de listas, de este modo, se puede entender una lista de listas como una matriz. Así, para acceder a un elemento i,j de la matriz, se debe acceder a: matriz[i][j].

Para ese ejercicio se dispone de un tablero de buscaminas especial, donde lo único que hay es bombas en las distintas posiciones. Este tablero es de la forma:

X		X
X			
X	X	
X			X
Donde las X representan las bombas. Ese tablero, en representación matricial de Python, donde se utilizan strings con un espacio: " " y "X" para representar espacios libres y bombas respectivamente, viene dado por:

tablero = [[' ', 'X', 'M', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
El objetivo de este ejercicio, es que programes una función buscaminas que reciba como argumento a una matriz tablero y dos coordenadas i, j, y que entregue la cantidad de bombas que rodean a esa posición.

Por ejemplo, si la el tablero dado es el representado en la tabla, y la posición viene dada por i=0 y j=0, tu función debe retornar el valor 2, ya que hay dos bombas rodeándola, en (0,1) y (1,0).

Por otro lado, si el tablero es el mismo, y las coordenadas son i=1, j=1, tu función debe retornar 4, pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y en (2,2).

Hint: recuerda que el tablero puede ser de un tamaño arbitrario y que al escribir posiciones más grandes que ese tamaño o menores que 0, tu programa arrojará error.
"""
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


