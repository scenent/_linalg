import numpy as np

# 역행렬을 구하려면?
# -> 수반행렬이 필요.
# 수반행렬을 구하려면?
# -> 여인수행렬을 전치하면 됨.
# 즉, 여인수행렬을 빠르게 구한다.

# A라는 3x3 행렬을 만들어둔다.
A = np.array([
	[1, 2, 3],
	[2, 5, 3],
	[1, 0, 8]
], dtype=float)

# 소행렬을 얻는다.
def get_minor(matrix, row, col):
    return np.delete(np.delete(matrix, row, axis=0), col, axis=1)

# 여인수행렬 (=cofactor matrix) 을 얻는다.
# 소행렬      M
# 소행렬'식'  M_ij
# 여인수행렬 A_ij = (-1**(i+j)) * M_ij
def cofactor_matrix(matrix):
    n = matrix.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            # 소행렬 얻고?
            minor = get_minor(matrix, i, j)
            # 소행렬식 M_ij
            C[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    return C

det_A = round(np.linalg.det(A))

if det_A == 0:
    print("행렬식이 0이므로, 역행렬이 존재하지 않습니다.")
else:
    # 여인수행렬 얻는다.
    C = cofactor_matrix(A)
    # 수반행렬을 얻는다.
    #  = 즉, 여인수행렬을 전치한다.
    adj_A = C.T # ????
    # 이제 역행렬 계산.                             (1/행렬식) * 수반행렬
    inverse_A = (1 / det_A) * adj_A

    C = np.round(C, 10)
    adj_A = np.round(adj_A, 10)
    inverse_A = np.round(inverse_A, 10)

    print("행렬 A")
    print(A)
    print("행렬식 det A")
    print(det_A)
    print("여인수행렬 C")
    print(C)
    print("수반행렬 adj A")
    print(adj_A)
    print("역행렬 inv A")
    print(inverse_A)
    print("검산 : ")
    print(np.round(A @ inverse_A, 10))
