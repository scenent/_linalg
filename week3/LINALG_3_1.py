# 두 정방행렬을 더한다.
def add_square_matrices(A, B):
  n = len(A) # Define n as the dimension of the square matrix

  # 두 행렬의 크기 확인
  if n == 0 or len(B) != n or len(A[0]) != n or len(B[0]) != n:
    raise ValueError("두 행렬은 비어 있지 않고 크기가 같아야 합니다.")

  # 각 행의 원소 개수가 n개인지 확인 : n x n 정방행렬 검사.
  if any(len(row) != n for row in A):
    raise ValueError("A는 정방행렬이어야 합니다.")

  if any(len(row) != n for row in B):
    raise ValueError("B는 A와 같은 크기의 정방행렬이어야 합니다.")

  # 결과를 저장할 n x n 행렬을 0으로 초기화
  C = [[0 for _ in range(n)] for _ in range(n)]

  # 같은 위치의 원소끼리 더함
  for i in range(n):
    for j in range(n):
      C[i][j] = A[i][j] + B[i][j]

  return C

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(add_square_matrices(A, B))

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

row_a = len(A)
col_a = len(A[0])
row_b = len(B)
col_b = len(B[0])

# A의 열 개수와, B의 행 개수가 다르면 안됨.
if col_a != row_b:
  raise ValueError("에러")

# C의 차원은 (A의 행 개수) x (B의 열 개수)여야 합니다.
# C = [[0 for _ in range(row_a)] for _ in range(col_b)]
C = [[0 for _ in range(col_b)] for _ in range(row_a)]

for i in range(row_a):
  for j in range(col_b):
    for k in range(col_a):
      C[i][j] += A[i][k] * B[k][j]

print(C)

#    [22, 28],
#    [49, 64],
#    [76, 100],
#    [103, 136]

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

diagonal_sum = matrix[0][0] + matrix[1][1] + matrix[2][2]

print("대각합:", diagonal_sum)

import numpy as np

matrix = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
])

print(np.trace(matrix))