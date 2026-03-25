import random

# In each of the N steps, we add at least one, so after N steps we reach at least N

def create_T(N, K):
    # T = [(random.randint(1, K), random.randint(1, K)) for _ in range(N)]
    T = [(random.randint(1, K), random.randint(1, K), random.randint(1, K)) for _ in range(N)]
    # T = [(random.randint(1, K//1), random.randint(K//3, K//), random.randint(K//2, K)) for _ in range(N)]
    return T
