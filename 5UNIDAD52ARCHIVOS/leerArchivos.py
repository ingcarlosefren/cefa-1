def abrirArchivo():
  a=open("ejemplo.txt", "r")
  texto=a.read()
  a.close()
  return texto

def editarArchivo():
  a=open("ejemplo.txt", "w")
  a.write("esto es un texto nuevo")
  a.close()

def leerunarchivo():
  s = input("Ingresa nombre archivo: ")
  t = open(s)
  l = t.readline()
  while l!="":
    print(l)
    l=t.readline()
