import numpy as np

A = np.array([
    [1, 0, 2],
    [2, -1, 3],
    [4, 1, 8]
])

B = np.array([
    [-11, 2, 2],
    [-4, 0, 1],
    [6, -1, -1]
])

I = np.eye(3, dtype=int)

AB = A @ B
BA = B @ A

print("A = ")
print(A)

print("B = ")
print(B)

print("AB = ")
print(AB)

print("BA = ")
print(BA)

print("AB = I인가?", np.array_equal(AB, I))
print("BA = I인가?", np.array_equal(BA, I))

if np.array_equal(AB, I) and np.array_equal(BA, I):
    print("A와 B는 서로 역행렬이다.")
    print("즉, B = A^-1 이고 A = B^-1 이다.")
else:
    print("A와 B는 서로 역행렬이 아니다")
