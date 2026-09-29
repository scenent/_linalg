import numpy as np

A = np.array([
    [1, 2],
    [1, 3]
], dtype=float)

B = np.array([
    [3, 2],
    [2, 2]
], dtype=float)

A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

AB = A @ B


# 좌변은 A와 B의 곱 의 역.
left = np.linalg.inv(AB)

# 우변은 B의 역과 A의 역의 곱.
right = B_inv @ A_inv

np.set_printoptions(precision=3, suppress=True)

print("A^-1 = ")
print(A_inv)

print("B^-1 = ")
print(B_inv)

print("AB = ")
print(AB)

print("(AB)^-1 = ")
print(left)

print("B^-1 * A^-1 = ")
print(right)

print("AB의 역은, B의 역과 A의 역의 곱인가?")
print(np.allclose(left, right))
