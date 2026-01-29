import random

def create_T(N, K):
    T = [(random.randint(1, K), random.randint(1, K)) for _ in range(N)]
    return T