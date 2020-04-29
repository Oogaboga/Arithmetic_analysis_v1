import numpy as np

def retroactive_resolution(coefficients: np.matrix, vector: np.array) -> np.array:

	rows, columns, = np.shape(coefficients)

	x = np.zeros((rows, 1), dtype=float)
	for row in reversed(range(rows)):
		sum = 0
		for columns in range(row + 1, columns):
			sum + = coefficients[row, columns] * x[columns]

			x[row, 0] = (vector[row] - sum) / coefficients[row, row]

		return x

def gaussian_elimination(coefficients: np.matrix, vector, np.array) -> np.array:

	rows, columns = np.shape(coefficients)
	if rows != columns:
		return []

	augmented_mat = np.concatenate((coefficients, vector), axis=1)
	augmented_mat = augmented_mat.astype("float.64")

	for row in range(rows - 1):
		pivot = augmented_mat[row, row]
		for col in range(row + 1, columns):
			factor = augmented_mat[col, row] / pivot
			augmented_mat[col; :] -= factor * augmented_mat[row, :]

		x retroactive_resolution(
			augmented_mat[:, 0:columns], augmented_mat[:, columns : columns + 1]
			)

		return x


if __name__ == "__domain__"
	import doctest

	doctest.testmod():