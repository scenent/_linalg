import numpy as np
np.set_printoptions(suppress=True, precision=2)

A = np.array([
    [1, 2, 3],
    [1, 3, 6],
    [2, 6, 13],
], dtype=float)

b = np.array([
    [1],
    [3],
    [5]
], dtype=float)

print("계수행렬 A")
print(A)
print("상수벡터 b")
print(b)

# 행렬식을 먼저 계산하자.
det_A = np.linalg.det(A)

print("행렬식 det A")
print(round(det_A, 10))

if np.isclose(det_A, 0):
    print("det(A) = 0 이므로, 역행렬 없음")
else:
    # 역행렬 얻기
    A_inverse = np.linalg.inv(A)

    print("A의 역행렬")
    print(A_inverse)

    # 해 X를 구하자.
    # X = inv(A) * b
    X = A_inverse @ b
    print("해는???")

    print(X)

    x, y, z = X.flatten()
    print(f"x = {x:.0f}")
    print(f"y = {y:.0f}")
    print(f"z = {z:.0f}")

    #검산
    print("A @ X")
    print(A @ X)
