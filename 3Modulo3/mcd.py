"""Pregunta 1
Existen múltiples formas de calcular el máximo común divisor de un conjunto de números, escriba una función de nombre mcd que reciba dos números n1 y n2 como argumentos, y retorne el máximo común divisor. Por ejemplo para los argumentos 10 y 15 debe retornar 5."""

"""la solucion a este ejercicio se realiza utilizando el algoritmo de euclides, el cual consiste en dividir el mayor numero entre el menor numero hasta que el residuo sea 0, el maximo comun divisor sera el numero menor divisor""" 

def mcd(n1,n2):
  if n1>=n2:
    if n1%n2==0:
      return n2
    else:
      while n1%n2!=0:
        r=n1%n2
        n1=n2
        n2=r
        mcd=n2
  else:
    if n2%n1==0:
      return n1
    else:
      while n2%n1!=0:
        r=n2%n1
        n2=n1
        n1=r
        mcd=n1

  return mcd

mcd(10,15)