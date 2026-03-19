
from game import create_T

class LookUpTable:
    def __init__(self):
        self.lut = {}
    
    def print(self):
        for key, value in self.lut.items():
            print(f"{key}: {value}")
    
    def get(self, s, ns, myTurn):
        return self.lut.get((s, ns, myTurn), None)
    
    def clear(self):
        self.lut.clear()
    
    def populate(self, N, T, max_steps):
        self.clear()
        self.creation_steps = 0
        if max_steps > 0:
            self.recursive_iteration(N, T, max_steps)
        return self.creation_steps

    # def get_possible_ns(self, N, K):
    def get_possible_ns(self, N):
        possible_ns = [[] for _ in range(N)]
        # produces N-1, ..., 0
        for step in range(N-1, -1, -1):
            for ns in range(step, N):
                # because on step 0 ns is always 0
                if step == 0:
                    possible_ns[step].append(0)
                    break
                # because then is ns larger then reachable by adding K to the previous step
                # needs K as argument
                # if ns > step-1+K:
                #     continue
                possible_ns[step].append(ns)
        return possible_ns

    def recursive_iteration(self, N, T, max_steps):
        possible_ns = self.get_possible_ns(N)
        # produces N-1, ..., 0
        for step in range(N-1, -1, -1):
            if N-step > max_steps:
                break
            for ns in possible_ns[step]:
                self.creation_steps += 2
                Ts0 = T[step][0]
                Ts1 = T[step][1]
                isWinning = ns+Ts0 >= N or ns+Ts1 >= N
                self.lut[(step, ns, True)] = 1 if isWinning else max([self.lut[(step+1,  ns+Ts0, False)], self.lut[(step+1, ns+Ts1, False)]])
                self.lut[(step, ns, False)] = 0 if isWinning else min([self.lut[(step+1, ns+Ts0, True)], self.lut[(step+1, ns+Ts1, True)]])


def main():
    N = 100
    K = 8
    MAX_STEPS = 4
    T = create_T(N, K)
    lut = LookUpTable()
    # print(lut.get_possible_ns(N))
    lut.populate(N, T, MAX_STEPS)
    lut.print()

if __name__ == "__main__":
    main()
