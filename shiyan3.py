import math


def power_mod(base, exponent, modulus):
    return pow(base, exponent, modulus)


def dh_key_exchange(p, g, a, b):
    # 计算公钥
    A = power_mod(g, a, p)
    B = power_mod(g, b, p)

    # 计算共享密钥
    K_A = power_mod(B, a, p)
    K_B = power_mod(A, b, p)

    return A, B, K_A, K_B


# 设置参数
p = 101
g = 2
a = 5
b = 7

# 调用函数
A, B, K_A, K_B = dh_key_exchange(p, g, a, b)

# 输出结果
print(f"公钥 A: {A}")
print(f"公钥 B: {B}")
print(f"共享密钥 K_A: {K_A}")
print(f"共享密钥 K_B: {K_B}")