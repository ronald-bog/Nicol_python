''' IF '''
'''
if - else

if condicion:
    # bloque a ejecutar si if true
else: * no evalua condiciones
   # bloque a ejecutar si if es false 
'''

# elif si evalua condicion

edad = 18
""" if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

if edad >= 18:
    print('Eres mayor de edad')
elif edad < 18 and edad > 12:
    print('Eres un adolescente')
else:
    print('Eres un niño') """
    
if edad >= 18:
    print('Eres mayor de edad')

if edad < 18 and edad > 12:
    print('Eres un adolescente')
else:
    print('Eres un niño')

''' if Anidado '''

edad = 21
pais = 'Colombia'

if edad >= 21:
    if pais == 'EEUU':
        print('Si puedes votar en USA')
    else:
        print('Pero si puedes votar en Colombia')
else:
    print('No puedes votar')

''' Expresion Ternaria if - else'''
# Sintaxis: 'bloque true' if condicion else 'bloque false'

""" if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad') """

print('Eres mayor de edad' if edad >= 18 else 'Eres menor de edad')

# (Java) edad >= 18 else ? 'Eres mayor de edad' : 'Eres menor de edad';