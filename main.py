#Jose Leonardo Perez Gonzalez
#A01424133

#algoritmo de cifrado de cesar
text = input("introduce el texto a cifrar: ")
text = text.upper() #convertimos todo a mayusculas
value =  input("Introduce el caracter que sera el inicio del abecedario: ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


des = alphabet.find(value.upper()) #obtenemos el valor numerico de la letra

encrypted = ""

for char in text:
  if char in alphabet:
    encrypted += alphabet[ (alphabet.index(char)+ des ) % len(alphabet)]
  else:
    encrypted +=char

print("el cifrado es: ", encrypted.lower())
