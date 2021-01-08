def PedirDatos():
  # Solicitud de nombre
  nombre = input("Para empezar, dime como te llamas. ")
  print()
  print("Hola ", nombre, ", bienvenido a Mi Red")
  print()

  # CÃ¡lculo de edad
  agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
  edad = 2017-agno-1
  print()

  # CÃ¡lculo de estatura
  estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
  estatura_m = int(estatura)
  estatura_cm = int( (estatura - estatura_m)*100 )

  # Cantidad de amigos
  num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
  
  
def MostrarDatos():
  print("--------------------------------------------------")
  print("Nombre:  ", PedirDatos.nombre)
  print("Edad:    ", PedirDatos.edad, "aÃ±os")
  print("Estatura:", PedirDatos.estatura_m, "metros y", PedirDatos.estatura_cm, "centÃ­metros")
  print("Amigos:  ", PedirDatos.num_amigos)
  print("--------------------------------------------------")
  print()