# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (" \n Bienvenidos  a mi trivia ")
print (" Pondremos a prueba tus conocimientos ")

# Es importante dar instrucciones sobre cómo jugar:
print ("\n Siga las Siguientes Instrucciones:\n")
print (" Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("\n1) ¿Quién es el actual presidente del Perú? : ")
print ("a) Antauro Humala")
print ("b) Valentin Paniagua")
print ("c) Alan Garcia")
print ("d) Pedro Castillo")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

# Pregunta 2
print ("\n1) ¿Cuando es el dia se celebra la independencia de Perú? : ")
print ("a) 28 de Julio ")
print ("b) 19 de Mayo")
print ("c) 14 de Abril")
print ("d) 4 de Diciembre")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_2 = input("\nTu respuesta: ")

# Pregunta 3
print ("\n1) ¿Que año se proclamo la Independecia del Perú? : ")
print ("a) 1924")
print ("b) 1759")
print ("c) 1821")
print ("d) 1870")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_3 = input("\nTu respuesta: ")

# Evaluamos si la respuestas son correcta 
if respuesta_1 == "d":
  print("\nLa Respuesta a la Pregunta 1 ")
  print("\nEs Correcto! ")
else:
  print("\nLa Respuesta a la Pregunta 1 ")
  print("\nEs Incorrecto! ")

if respuesta_2 == "a":
  print("\nLa Respuesta a la Pregunta 2 ")
  print("\nEs Correcto! ")
else:
  print("\nLa Respuesta a la Pregunta 2 ")
  print("\nEs Incorrecto! ")

if respuesta_3 == "c":
  print("\nLa Respuesta a la Pregunta 3 ")
  print("\nEs Correcto! ")
else:
  print("\nLa Respuesta a la Pregunta 3 ")
  print("\nEs Incorrecto! ")