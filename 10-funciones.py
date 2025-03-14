# FUNCIONES

# funciones void

def miFuncion():
    print(5+5)


# miFuncion()


def saludar(nombre):
    print(f'Hola como estas {nombre}')


# saludar('Nicol')

palabras = ['for', 'if', 'def']
# print(palabras)


def palabrasReservadas(word, w2):
    palabras.append(word)
    palabras.append(w2)


palabrasReservadas('in', 'fsed')

# print(palabras)


# recibiendo = miFuncion()
# print(recibiendo)

# funciones con retorno


def restar(a, b):
    num1 = a
    num2 = b
    return num1 - num2


recibiendo2 = restar(100, 75)
print(recibiendo2)


# Retorno multiple

def multiple():
    n1 = 10
    n2 = 5
    return [n1, n2]


# print(multiple())

# desempaquetamiento (desestructuracion)

n1, n2 = multiple()
print(n1)
print(n2)

# Parametros por defecto


def porDefecto(nombre, saludo='Hola'):
    mensaje = f'{saludo} {nombre}'
    return mensaje


print(porDefecto('Monica', 'Como estas'))
