
from game import create_T

lut = {}

def payoff(N, T, step, max_steps):
    Ts0 = T[step][0]
    Ts1 = T[step][1]
    
    # N-step to N-1
    for i in range(1, step+1):
        # (step, ns, Tchoice, myTurn)
        lut[(step, N-i, Ts0, True)] = 1 if N-i+Ts0 >= N else min([lut[(step-1, N-i+Ts0, T[step-1][0], False)], lut[(step-1, N-i+Ts0, T[step-1][1], False)]])
        lut[(step, N-i, Ts0, False)] = 0 if N-i+Ts0 >= N else max([lut[(step-1, N-i+Ts0, T[step-1][0], True)], lut[(step-1, N-i+Ts0, T[step-1][1], True)]])
        
        lut[(step, N-i, Ts1, True)] = 1 if N-i+Ts1 >= N else min([lut[(step-1, N-i+Ts1, T[step-1][0], False)], lut[(step-1, N-i+Ts1, T[step-1][1], False)]])
        lut[(step, N-i, Ts1, False)] = 0 if N-i+Ts1 >= N else max([lut[(step-1, N-i+Ts1, T[step-1][0], True)], lut[(step-1, N-i+Ts1, T[step-1][1], True)]])
    
    if step == max_steps:
        return
    payoff(N, T, step+1, max_steps)



def create_lookup_table(N, T, max_steps):
    lut.clear()
    payoff(N, T, 1, max_steps)
    return lut

if __name__ == "__main__":
    N = 23
    K = 5
    MAX_STEPS = 3
    T = create_T(N, K)
    print(create_lookup_table(N, T, MAX_STEPS))