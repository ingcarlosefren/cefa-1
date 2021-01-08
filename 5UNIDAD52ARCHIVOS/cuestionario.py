a = "votar"
b = a.replace("v","n")
print(b)

####

a = "oso pardo"
b = a.strip("o")
print(b)


#escribe las pablas al rever
s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i<len(s):
  resultado= resultado + s[len(s)-i-1]
  i=i+1
print(resultado)

#######################
def mezclador(string_a, string_b):
  # aquí debes escribir el código de tu programa
  texto=string_a[0:2]+string_b[-2:]
  return  texto# aquí debes retornar el resultado

print(mezclador("familia","abrigarse"))


######################
def intercalar(string_a, string_b):
  i=0
  nuevotexto=""
  while i<len(string_a):
    nuevotexto=nuevotexto + string_a[i]+string_b
    i=i+1
  return nuevotexto # aquí debes retornar el resultado

print(intercalar("paz","so"))

#######################

"""
Pregunta 3
Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.

Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)

"""

def ocurrencias(string):
  i=0
  unos=0
  cero=0
  while i<len(string):
    if "1" in string[i]:
      unos=unos+1
      i=i+1
    elif "0" in string[i]:
      cero=cero+1
      i=i+1
    else:
      print(string[i],"no es un numero valido en la posicion: ", i)
      i=i+1
#Ahora realizo la resta validando cual es mayor      
  if unos>=cero:
    Resultado=unos-cero
  else:
    Resultado=cero-unos

  return Resultado # aquí debes retornar el resultado

print(ocurrencias("1100011010"))


####################

"""
Pregunta 4
Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el elemento en el índice n.

Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".

Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.
"""
def remover_enesimo(s, n):
  i = 0
  resultado=""
  while i<len(s):
    if n>len(s):
      resultado= resultado + s[i]
      i=i+1
    else:
      if i==n:
        resultado= resultado + ""
        #print(resultado)
        i=i+1
      else:
        resultado= resultado + s[i]
        i=i+1
        #print(resultado)

  return resultado # aquí debes retornar el resultado

print(remover_enesimo("Hasta luego", 3))

#######################

"""
Pregunta 5
Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.

Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".

"""
def reemplazo(string):
  TexMayus=string.upper()
  i=0
  NuevoText=""
  while i<len(string):
    if string[i]==TexMayus[i]:
      if string[i]==" ":
        NuevoText=NuevoText+" "
        i=i+1
      else:
        NuevoText=NuevoText+"$"
        i=i+1
    else:
      NuevoText=NuevoText+string[i]
      i=i+1

  return NuevoText # aquí debes retornar el resultado

print(reemplazo("Paz es Paz"))