import random

# In each of the N steps, we add at least one, so after N steps we reach at least N

def create_T(N, K):
    T = [(random.randint(1, K), random.randint(1, K)) for _ in range(N)]
    # T = [(random.randint(1, K), random.randint(1, K), random.randint(1, K)) for _ in range(N)]
    # T = [(random.randint(1, K//2), random.randint(K//2, K)) for _ in range(N)]
    # return [(1,2), (2,3), (1,2), (1,3), (1,2)]
    # return [(1, 2), (1, 1), (2, 1), (1,2), (1,2)]
    return T
