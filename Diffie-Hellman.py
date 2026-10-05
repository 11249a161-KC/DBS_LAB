import random

def diffie_hellman():
    p = 23
    g = 5
    a = random.randint(2, p - 2)
    A = pow(g, a, p)
    b = random.randint(2, p - 2)
    B = pow(g, b, p)
    secret_A = pow(B, a, p)
    secret_B = pow(A, b, p)

    print("Diffie-Hellman Key Exchange")
    print(f"   Public prime (p)   : {p}")
    print(f"   Generator (g)      : {g}")
    print(f"   Alice private (a)  : {a} Public A: {A}")
    print(f"   Bob private (b)    : {b} Public B: {B}")
    print(f"   Alice shared key   : {secret_A}")
    print(f"   Bob shared key     : {secret_B}")
    print(f"   Keys Match         : {secret_A == secret_B}")

diffie_hellman()
