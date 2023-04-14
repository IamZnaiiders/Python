""" Metodos de cadena de texto """

cadena_1 = "mi nombre es esnaider "
cadena_2 = "Bienvenido a mi curso"
numbers = "123980"

"DIR: DEVUELVE LA LISTA DE ATRIBUTOS VALIDOS DEL OBJETO PASADÓ"
dir(cadena_1)

# Metodos que transforman un valor

'El metodo upper() transforma todas las letras a mayusculas de un texto.'
resultado = cadena_1.upper()

'El metodo lower() convierte todas las letras en minusculas'
min = cadena_2.lower()

'El metodo capitaliza() convierte la primera letra a mayuscula'
pri_letra_mayuscula = cadena_1.capitalize()


# Metodos de buscan un valor

'El metodo find() encuentra la primera aparicion del valor especificado sino devulve -1. Devulve la posicion que nosotros le indiquemos'
buscar = cadena_1.find("es")

'El metodo index() busca una cadena dentro de otra cadena. La diferencia es en caso de no encontrar una coincidencia nos devulve un error.'
index = cadena_1.index("m")


print("Mayusculas: "+resultado)
print("Minusculas => " + min)
print("Primera letra en mayuscula => " + pri_letra_mayuscula)
print("Metodo buscar => " + str(buscar))
print("Metodo INDEX => " + str(index))

'Un metodo es una funcion aplicada a un objeto'

# Metodos que consultan un valor
'Si es numerico devolvemos TRUE y si no FALSE'
is_numerico = numbers.isnumeric()

'Si es alfa numerico'
print(is_numerico )
