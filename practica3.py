def mas_repetido(matriz):
    pass

def condensa(cadena):
	if cadena:
		ocurrencias = 0
		i = 0
		lista = []
		while len(cadena) > 0:
			ocurrencias += 1
			while i + 1 < len(cadena) and cadena[i + 1] == cadena[i]:
				ocurrencias += 1
				i += 1
			i = 0
			lista.append((cadena[0], ocurrencias))
			cadena = cadena.replace(cadena[0], "", ocurrencias)
			ocurrencias = 0
		return lista
	else:
		return []

def triangulo_pascal(niveles):
    lista = []
    lista.append()

def subcadenas(cadena):
    pass
