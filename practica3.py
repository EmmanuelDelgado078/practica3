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
		for i in range(len(lista)):
		print(lista[i])
	else:
		print([])

def triangulo_pascal(niveles):
    lista = []
    lista.append()

def subcadenas(cadena):
	if cadena == []:
		return [[]]
	ll = lattice(cadena[1:])
	a =([e+[cadena[0]] for e in ll] + ll)
	print(a)
	return a

def mas_repetido_s():
	print("Por favor ingresa la matriz")
	y = input()
	mas_repetido(y)

def condensa_s():
	print("Por favor ingresa la cadena")
	n = input()
	condensa(n)

def triangulo_s():
	print("Por favor ingresa el nivel al que quieres llegar")
	m = input()
	triangulo_pascal(m)

def subcadenas_s():
	print("dame la cadena con esta estructura ['caracter','caracter','caracter']" +
    " con tantos caracteres como desees separados por comas u entre comillas simples")
	x = input()
	subcadenas(x)

def checar_funcion(n):
	switcher = {
		1: mas_repetido_s,
		2: condensa_s,
		3: triangulo_s,
		4: subcadenas_s
	}
	funcion = switcher.get(n, "Por favor ingresa un numero valido")
	#funcion = switcher[n]
	funcion()
	main()

def main():
	print("\nBienvenido al programa")
	print("Por favor ingresa el numero que corresponda a la funcion que quieres utilizar\n\n")
	print("1. Mas repetido: esta funcion encuentra el valor que mas repeticiones tiene en una matriz. Si dos numeros aparecen la misma cantidad de veces, devuelve el que aparece primero\n\n")
	print("2. Condensa: Esta funcion devuelve una lista con la letra y la cantidad de veces que aparece\n\n")
	print("3. Triangulo de pascal: esta funcion delvuelve una lista con los niveles del triangulo de pascal\n\n")
	print("4. subcadenas: Esta funcion devuelve una lista con la cadena dividida en subcadenas de tamano i\n\n")
	z = int(input())
	checar_funcion(z)

if __name__ == "__main__":
	main()
