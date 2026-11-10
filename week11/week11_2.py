import numpy as np

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")


# 7-1
print("7-1")
A = np.array([
    [2, 3],
    [3, -6]
])
coefficients = np.poly(A)
eigenvalues, X = np.linalg.eig(A)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]
print("특성다항식 계수")
print(coefficients)
print("고유값들")
print(eigenvalues)


# 7-2
print()
print("7-2")
A = np.array([
    [3, 2],
    [3, -2]
])
eigenvalues, X = np.linalg.eig(A)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]
print("고유벡터")
print(X)
print("고유값")
print(eigenvalues)

# 7-3
print()
print("7-3")
A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
])
eigenvalues, X = np.linalg.eig(A)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]
print("고유벡터")
print(X)
print("고유값")
print(eigenvalues)



# 7-4
print()
print("7-4")
A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
], dtype=float)
eigenvalues, X = np.linalg.eig(A)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]
_lambda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")
print("X = ")
print(X)
print("\nlambda = ")
print(_lambda)
