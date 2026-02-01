
from game import create_T

class LookUpTable:
    def __init__(self):
        self.lut = {}
    
    def get(self, s, ns, Ti):
        return self.lut.get((s, ns, Ti, True), None)
    
    def clear(self):
        self.lut.clear()
    
    def populate(self, N, T, max_steps):
        self.clear()
        if max_steps > 0:
            self.recursive_iteration(N, T, 1, max_steps)

    def recursive_iteration(self, N, T, s, max_steps):
        step = N-s-1
        if step < 0:
            return
        # TODO: are the step indices correct? They might be off by one too much
        Ts0 = T[step][0]
        Ts1 = T[step][1]
        
        # N-step to N-1
        for i in range(1, s+1):
            # (step, ns, Tchoice, myTurn)
            wins0 = N-i+Ts0 >= N
            wins1= N-i+Ts1 >= N
            self.lut[(step, N-i, Ts0, True)] = 1 if wins0 else min([self.lut[(step+1, N-i+Ts0, T[step+1][0], False)], self.lut[(step+1, N-i+Ts0, T[step+1][1], False)]])
            self.lut[(step, N-i, Ts0, False)] = 0 if wins0 else max([self.lut[(step+1, N-i+Ts0, T[step+1][0], True)], self.lut[(step+1, N-i+Ts0, T[step+1][1], True)]])
            self.lut[(step, N-i, Ts1, True)] = 1 if wins1 else min([self.lut[(step+1, N-i+Ts1, T[step+1][0], False)], self.lut[(step+1, N-i+Ts1, T[step+1][1], False)]])
            self.lut[(step, N-i, Ts1, False)] = 0 if wins1 else max([self.lut[(step+1, N-i+Ts1, T[step+1][0], True)], self.lut[(step+1, N-i+Ts1, T[step+1][1], True)]])
        
        if s == max_steps:
            return
        self.recursive_iteration(N, T, s+1, max_steps)
    
    def print(self):
        for key, value in self.lut.items():
            print(f"{key}: {value}")

def main():
    N = 5
    K = 3
    MAX_STEPS = 2
    T = create_T(N, K)
    lut = LookUpTable()
    lut.populate(N, T, MAX_STEPS)
    lut.print()

if __name__ == "__main__":
    main()
