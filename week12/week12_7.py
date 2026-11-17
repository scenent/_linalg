import numpy as np

u = np.array([1, 2], dtype=float)
v = np.array([6, -3], dtype=float)

dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

print(f"내적 = {dot_product:.6f}")

if norm_u == 0 or norm_v == 0:
    print("반드시 직교함. 영벡터 포함됨")
else:
    cos_theta = np.degrees(np.arccos(cos_theta))
    is_orthogonal = np.isclose(cos_theta, 0.0, ato1=1e-10, rto1=0.0)

    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"각도 = {theta_deg:.6f}도")
    print("직교합니다" if is_orthogonal else "직교하지 않습니다.")