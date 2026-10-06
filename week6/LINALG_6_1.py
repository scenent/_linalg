import numpy as np
np.set_printoptions(suppress=True, precision=2)

A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
], dtype=float)

I = np.eye(3)

# 첨가행렬.
# 가우스소거법 그거.
# 계수뽑고, 단위행렬 붙여놓은
AI = np.hstack((A, I))

def show_matrix(operation):
    print(f"{operation}")
    print(AI)

print("초기 첨가행렬 [A | I]")
print(AI)

# 첫번째 열에서,바로 밑에 원소를 0으로
AI[1] = (-2) * AI[0] + AI[1]
show_matrix("R2 <- (-2)R1 + R2")

AI[2] = (-1) * AI[0] + AI[2]
show_matrix("R3 <- (-1)R1 + R3")

# 두번째 열 기준, 아래원소 0으로
AI[2] = (2) * AI[1] + AI[2]
show_matrix("R3 <- (2)R2 + R3")

# 세번째 피벗 1로
AI[2] = (-1) * AI[2]
show_matrix("R3 <- (-1)R3")

# 세번째 열 피벗 위를 0으로
AI[1] = AI[1] + 3 * AI[2]
show_matrix("R2 <- R2 + 3R3")

AI[0] = AI[0] - 3 * AI[2]
show_matrix("R1 <- R1 - 3R3")

# 두번째 열, 피벗 위를 0으로
AI[0] = AI[0] - 2 * AI[1]
show_matrix("R1 <- R1 - 2R2")

A_inverse = AI[:, 3:]

print("최종 첨가행렬 [I | inv_A]")
print(AI)

print("inv A")
print(A_inverse)

print("역행렬 검산")
print(A @ A_inverse)
