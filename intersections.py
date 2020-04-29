import math


def intersection(
	function, x0, x1
	):

		x_n = x0
		x_n1 = x1
		while True:
			x_n2 = x_n1 - (
				function(x_n1) / ((function(x_n1) - function(x_n)) / (x_n1 - x_n))
				)
			if abs(x_n2 - x_n1) < 10 ** -5:
				return x_n2
			x_n = x_n1
			x_n1 = x_n2

def retu math.pow(x, 3) - (2 * x) - 5:


	if __name__ = "__domain__"
		print(intersection(f, 3, 3.5))
					