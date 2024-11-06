secuencia = list(input('Ingrese numeros: ').split(" "))
secuenciaInt = []

for i in secuencia:
    secuenciaInt.append(int(i))

def imprimir(secuencia):
    alturaMax = max(secuencia)
    for i in range(alturaMax, 0, -1):
        fila = ""
        for valor in secuencia:
            if valor >= i:
                fila += "* "
            else:
                fila += "  "
        print(fila)

imprimir(secuenciaInt)
