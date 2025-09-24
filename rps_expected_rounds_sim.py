# imports
import random as rand

# global variables
rounds_avg_3 = 0
rounds_avg_5 = 0
rounds_sum = 0
avg_rounds = 0
total_avg_rounds = 0

# hyperparemeters
iterations = 1000000

def play_game(total_rounds):
    p1_wins = 0
    p2_wins = 0
    rounds = 0
    while p1_wins <= (total_rounds//2)+1 and p2_wins <= (total_rounds//2)+1:
        vict = rand.randint(1, 3)
        if vict == 1:
            p1_wins += 1
        elif vict == 2:
            p2_wins += 1
        rounds += 1
    #print(rounds)
    #print(f"p1: {p1_wins} || p2: {p2_wins}")
    return rounds

# approximate the average amount of rounds for a best-of-three game
for i in range(iterations):
    rounds_sum += play_game(3)
rounds_avg_3 = rounds_sum / iterations

rounds_sum = 0

# approximate the average amount of rounds for a best-of-five game
for i in range(iterations):
    rounds_sum += play_game(5)
rounds_avg_5 = rounds_sum / iterations

# 4 best of three games, 1 best of 5 game
total_avg_rounds = 4*rounds_avg_3 + rounds_avg_5

# print!!! yaho
print(total_avg_rounds)
