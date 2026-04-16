
from math import ceil
import random
CHOICE_RANGE = [1, 100]
# random chance for the player to give a mainstream answer, otherwise there are to many players answering 1
# main stream answers: Players that answer on 100*(2/3)^n
MAIN_STREAM_ANSWER_CHANCE = 0.8

MEAN_ANSWER = 30
SIGMA_SCALE = 30

def get_random_mainstream_answer():
    stream_selection_random = random.uniform(0,1)
    if stream_selection_random < (3/9):
        return 22
    elif stream_selection_random < (6/9):
        return 33
    elif stream_selection_random < (8/9):
        return 55
    else:
        return 67

class Player:
    id = -1
    noise_range = 0 # random number from range is added or subtracted from answer
    answer = 0
    score = 0

    def __init__(self, id):
        self.id = id
        self.score = 0

    def add_win(self):
        self.score += 1
    
    # Starting from a random answer a player with thinking_depth closer to 1 will do more 2/3 multiplications
    def give_answer(self, mean_answer=MEAN_ANSWER, sigma_scale=SIGMA_SCALE):
        gaussian_answer = round(random.gauss(mean_answer, sigma_scale))
        gaussian_answer = max(CHOICE_RANGE[0], min(CHOICE_RANGE[1], gaussian_answer))
        if gaussian_answer == CHOICE_RANGE[0] and random.uniform(0,1) < MAIN_STREAM_ANSWER_CHANCE:
            return get_random_mainstream_answer()
        elif gaussian_answer == CHOICE_RANGE[0] and random.uniform(0,1) < 0.5:
            return random.uniform(15, 35)
        if gaussian_answer == CHOICE_RANGE[1] and random.uniform(0,1) < 0.75:
            return self.give_answer(MEAN_ANSWER, sigma_scale // 4)
        return gaussian_answer
        
def main():
    answers = []
    lowest_answer = 100
    for id in range(100):
        player = Player(id=id)
        answers.append(player.give_answer())
        print(f"{player.answer}")
        if player.answer < lowest_answer:
            lowest_answer = player.answer
    print(f"Average answer: {sum(answers)/len(answers)}")
    print(f"Lowest answer: {lowest_answer}")
if __name__ == "__main__":
    main()