import random

def create_T(N, K, numberOfOptions=2, isKDefivided=False):
    T = []
    for _ in range(N):
        options = []
        for i in range(numberOfOptions):
            if isKDefivided:
                options.append(random.randint(1+i*(K//numberOfOptions), (i+1)*(K//numberOfOptions)))
            else:
                options.append(random.randint(1, K))
        T.append(tuple(options))
    return T
