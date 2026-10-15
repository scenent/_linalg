from fractions import Fraction


def print_matrix(name, M):
    """행렬을 보기 좋게 출력"""
    print(name)
    for row in M:
        print("[" + " ".join(f"{str(v):>5}" for v in row) + "]")
    print()


# 주어진 행렬
A = [
    [1, 2, 1],
    [2, 3, 3],
    [-3, -10, 2],
]

print_matrix("초기 행렬 A", A)

n = len(A)

# 분수의 정확한 계산을 위해 Fraction을 사용한다.
A = [[Fraction(v) for v in row] for row in A]
U = [row[:] for row in A]

# L은 단위행렬에서 시작한다.
L = [
    [Fraction(1 if i == j else 0) for j in range(n)]
    for i in range(n)
]

# 가우스 소거법으로 U를 만들고, 소거 배수를 L에 저장한다.
for k in range(n - 1):
    if U[k][k] == 0:
        raise ValueError("피벗이 0이므로 행 교환이 필요합니다.")

    for i in range(k + 1, n):
        multiplier = U[i][k] / U[k][k]
        L[i][k] = multiplier

        U[i] = [
            U[i][j] - multiplier * U[k][j]
            for j in range(n)
        ]

        print(f"R{i + 1} <- R{i + 1} - ({multiplier}) * R{k + 1}")
        print_matrix("현재 U", U)

print_matrix("최종 하삼각행렬 L", L)
print_matrix("최종 상삼각행렬 U", U)

# L과 U의 곱으로 원래 행렬을 검산한다.
LU = [
    [
        sum(L[i][k] * U[k][j] for k in range(n))
        for j in range(n)
    ]
    for i in range(n)
]

print_matrix("검산: L x U", LU)
print("LU = A 확인:", LU == A)