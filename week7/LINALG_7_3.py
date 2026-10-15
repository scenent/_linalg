def print_matrix(M):
    """계수와 각 시스템의 상수항을 구분하여 출력"""
    for row in M:
        print(f"[{row[0]:>3} {row[1]:>3} | {row[2]:>3} | {row[3]:>3}]")
    print()


# 두 연립방정식의 첨가행렬
# 시스템 1: x1 + 2x2 = 2,  3x1 + 7x2 = 8
# 시스템 2: x1 + 2x2 = 1,  3x1 + 7x2 = 7
# 열의 의미: [x1 계수, x2 계수, 시스템 1 상수항, 시스템 2 상수항]
M = [
    [1, 2, 2, 1],
    [3, 7, 8, 7],
]

print("1. 초기 첨가행렬")
print_matrix(M)

# R2 <- R2 - 3R1
M[1] = [M[1][i] - 3 * M[0][i] for i in range(4)]

print("2. R2 <- R2 - 3R1")
print_matrix(M)

# R1 <- R1 - 2R2
M[0] = [M[0][i] - 2 * M[1][i] for i in range(4)]

print("3. R1 <- R1 - 2R2")
print_matrix(M)

# 왼쪽 계수 행렬이 단위행렬이므로 각 상수항 열에서 해를 읽는다.
for system in range(2):
    column = 2 + system
    x1 = M[0][column]
    x2 = M[1][column]
    print(f"시스템 {system + 1}의 해: x1 = {x1}, x2 = {x2}")