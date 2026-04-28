
class LookUpTable:
    def __init__(self):
        self.lut = {}
    
    def print(self):
        for key, value in self.lut.items():
            print(f"{key}: {value}")
    
    def get(self, s, ns, myTurn):
        return self.lut.get((s, ns, myTurn), None)
    
    def populate(self, N, T, max_steps):
        self.lut.clear()
        self.computation_steps = 0
        if max_steps > 0:
            self.create_lut(N, T, max_steps)
        return self.computation_steps

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

    # N is the number of objects to be taken, T is the list of possible moves for each step, max_steps is the maximum number of steps to consider
    def create_lut(self, N, T, max_steps):
        possible_ns = self.get_possible_ns(N)
        # produces N-1, ..., 0
        for step in range(N-1, -1, -1):
            if N-step > max_steps:
                return
            # ns is the number of objects left to take, can be from step to N-1
            # in step 0, ns is always 0, in step N-1, ns can be from N-1 to N-1
            for ns in possible_ns[step]:
                move_options = T[step]
                self.computation_steps += len(move_options)

                can_win_now = any(ns + move >= N for move in move_options)
                if can_win_now:
                    # I immediately win
                    self.lut[(step, ns, True)] = 1
                    # Opponent immediately wins, so I lose.
                    self.lut[(step, ns, False)] = 0
                else:
                    # My turn: I pick a move that maximizes my winning chance.
                    next_values = [self.lut.get((step + 1, ns + move, False), 0) for move in move_options]
                    self.lut[(step, ns, True)] = max(next_values)
                    # Opponent turn: opponent picks a move that minimizes my winning chance.
                    next_values = [self.lut.get((step + 1, ns + move, True), 1) for move in move_options]
                    self.lut[(step, ns, False)] = min(next_values)
