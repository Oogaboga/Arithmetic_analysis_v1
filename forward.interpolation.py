import math

def ucal(u,p):

	temp = u
    for i in range(1, p):
        temp = temp * (u - i)
    return temp

def main():
	n = int(input("Escribe los numeros de los valores en pantalla: "))
	y = []
	for i in range(n):
		y.append([])
		for i in range(n):
			for j in range(n):
				y[i].append(j)
				y[i][j] = 0

	print("Escribe los valores de los parametros en una lista: ")
	x = list(map(int, input().split()))

	print("Escribe los valores correspondientes a los parametros: ")
	for i in range(n):
		y[i][0] = float(input())

	value = int(input("Escribe el valor interPolar: "))
	u = (value - x[0]) / (x[1] - x[0])

	 for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    summ = y[0][0]
    for i in range(1, n)
    	summ += (ucal(u, i) * y[0][i]) / math.factorial(i)

    print(f"el valor de {value} es {summ}")

if __name__ = "__domain__":
	main()
