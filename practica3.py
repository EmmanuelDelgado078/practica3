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
		for i in range(len(lista)):    print (lista[i])
	else:
		return []

def triangulo_pascal(niveles):
	if niveles > 0:
	    if niveles == 0:
	        return []
	    elif niveles == 1:
	        return [[1]]
	    else:
	        lista_1 = [1]
	        resultado = triangulo_pascal(niveles-1)
	        lista_2 = resultado[-1]
	        for i in range(len(lista_2)-1):
	            lista_1.append(lista_2[i] + lista_2[i+1])
	        lista_1 += [1]
	        resultado.append(lista_1)
	    for i in range(len(resultado)):    print (resultado[i])	
	else:
		print("No existen niveles negativos")

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
	main_aux()

def condensa_s():
	print("Por favor ingresa la cadena")
	n = input()
	condensa(n)
	main_aux()

def triangulo_s():
	print("Por favor ingresa el nivel al que quieres llegar")
	m = input()
	triangulo_pascal(m)
	main_aux()

def subcadenas_s():
	print("Por favor ingresa la cadena")
	x = input()
	subcadenas(x)
	main_aux()

def checar_funcion(n):
	switcher = {
		1: mas_repetido_s,
		2: condensa_s,
		3: triangulo_s,
		4: subcadenas_s
	}
	funcion = switcher.get(n, "Por favor ingresa un número válido")
	funcion()
	main()

def main_aux():
	print("¿Deseas continuar? S/n")
	z = input()
	z.lower()
	if z == "s":
		main()
	elif z == "n":
		sys.exit()
	else:
		"Por favor elige una opción válida"
		main_aux()


def main():
	print("\n¡Bienvenido al programa!")
	print("Por favor ingresa el número que corresponda a la función que quieres utilizar\n\n")
	print("1. Más repetido: esta función encuentra el valor que más repeticiones tiene en una matriz. Si dos números aparecen la misma cantidad de veces, devuelve el que aparece primero\n\n")
	print("2. Condensa: Esta función devuelve una lista con la letra y la cantidad de veces que aparece\n\n")
	print("3. Triangulo de pascal: esta función delvuelve una lista con los niveles del triangulo de pascal\n\n")
	print("4. subcadenas: Esta función devuelve una lista con la cadena dividida en subcadenas de tamaño i\n\n")
	z = int(input())
	checar_funcion(z)

if __name__ == "__main__":
	main()
