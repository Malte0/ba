
from math import ceil
import random
CHOICE_RANGE = [1, 100]

class Player:
    id = -1
    thinking_depth = 0 # [0,1]
    noise_range = 5 # random number from range is added or subtracted from answer
    answer = 0
    score = 0

    def __init__(self, id, thinking_depth):
        self.id = id
        self.thinking_depth = thinking_depth
        self.score = 0

    def add_win(self):
        self.score += 1
    
    # Starting from a random answer a player with thinking_depth closer to 1 will do more 2/3 multiplications
    def give_answer(self):
        answer = random.uniform(1,100)

        if self.thinking_depth > 0.99:
            return 1
        random_number = random.uniform(0,1)
        while random_number < self.thinking_depth:
            answer *= (2 / 3)
            random_number = random.uniform(0,1)
        answer_noised = answer + (random.uniform(-self.noise_range, self.noise_range))
        self.answer = max(min(answer_noised, CHOICE_RANGE[1]), CHOICE_RANGE[0])
        return self.answer

def main():
    answers = []
    for i in range(10000):
        player = Player(i, 0.6)
        answer = player.give_answer()
        answers.append(answer)
    print(f"Average answer: {sum(answers) / len(answers)}")

if __name__ == "__main__":
    main()