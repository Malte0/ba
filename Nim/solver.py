
from game import create_T

def payoff(n, T, max_steps):
    look_up_table = {}
    for step in range(1, max_steps):
        ts1 = T[n-step][0]
        ts2 = T[n-step][1]
        # (position, is_player_turn, tsi) = payoff
        look_up_table[(n-step, True, ts1)] = 1 if n-step+ts1 >= n else min(look_up_table[(n-step+ts1, False, ts1)], look_up_table[(n-step+ts1, False, ts2)])
        look_up_table[(n-step, True, ts2)] = 1 if n-step+ts2 >= n else min(look_up_table[(n-step+ts2, False, ts1)], look_up_table[(n-step+ts2, False, ts2)])
        look_up_table[(n-step, False, ts1)] = 0 if n-step+ts1 >= n else max(look_up_table[(n-step+ts1, True, ts1)], look_up_table[(n-step+ts1, True, ts2)])
        look_up_table[(n-step, False, ts2)] = 0 if n-step+ts2 >= n else max(look_up_table[(n-step+ts2, True, ts1)], look_up_table[(n-step+ts2, True, ts2)])

    return look_up_table

def create_lookup_table(n, T, max_steps):
    lookup_table = payoff(n, T, max_steps)
    return lookup_table

if __name__ == "__main__":
    MAX_STEPS = 3
    N, K, T, s = create_T(23, 5)
    print(create_lookup_table(N, T, MAX_STEPS))