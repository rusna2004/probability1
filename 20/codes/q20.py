import random

def throw_dice():
    return random.randint(1, 6)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def simulate_dice_rolls(num_simulations):
    count_sum_7 = 0
    count_prime = 0
    count_sum_1 = 0
    
    for _ in range(num_simulations):
        dice1 = throw_dice()
        dice2 = throw_dice()
        dice_sum = dice1 + dice2
        
        if dice_sum == 7:
            count_sum_7 += 1
        if is_prime(dice_sum):
            count_prime += 1
        if dice_sum == 1:
            count_sum_1 += 1
            
    prob_sum_7 = count_sum_7 / num_simulations
    prob_prime = count_prime / num_simulations
    prob_sum_1 = count_sum_1 / num_simulations
    
    return prob_sum_7, prob_prime, prob_sum_1

num_simulations = 100000  # Number of simulations

prob_sum_7, prob_prime, prob_sum_1 = simulate_dice_rolls(num_simulations)

print(f"Probability of sum being 7: {prob_sum_7:.4f}")
print(f"Probability of sum being prime: {prob_prime:.4f}")
print(f"Probability of sum being 1: {prob_sum_1:.4f}")

