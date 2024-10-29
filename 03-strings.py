marcaRopa = 'Diesel'

# Indices
print(marcaRopa[3])

# longitud
print(len(marcaRopa))

# METODOS
texto = 'python es dinamico'

print(texto.capitalize()) # Primera letra mayuscula
print(texto.strip()) # Quita espacios al comienzo y al final
print(texto.upper()) # mayusculas
print(texto.lower()) # minusculas
print(texto.title()) # primeras letras en mayusc
print(texto.replace('dinamico','facil')) 
print(texto.find('i'))
print(texto.count('i'))
#print(texto.zfill(30))

''' f-strings '''
nombre = 'Carlos'
mensaje = 'que tal tu dia'
print(f'Hola { nombre } como \n has estado, {mensaje}')

print('Hola como estas', nombre, ' que tal')

print('''
hola
como
estas
''')

''' INPUT '''
entrada = input('dame tu edad: ')

print(f'Tu es => {entrada}')