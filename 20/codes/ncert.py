import numpy as np
from scipy.stats import randint

# Simulate throwing two dice a large number of times
num_simulations = 1000000

# Simulate throwing two dice and calculate the probabilities
def simulate_dice_rolls(target_sum):
    dice1 = np.random.randint(1, 7, num_simulations)
    dice2 = np.random.randint(1, 7, num_simulations)
    successful_outcomes = np.count_nonzero(dice1 + dice2 == target_sum)
    probability = successful_outcomes / num_simulations
    return probability

# Calculate probabilities for different target sums
prob_sum_7 = simulate_dice_rolls(7)

def is_prime(num):
    if num <= 1:
        return False
    divisors = np.arange(2, int(np.sqrt(num)) + 1)
    return np.all(num % divisors != 0)

prime_sums = [2, 3, 5, 7, 11]
prob_prime_sum = np.sum([simulate_dice_rolls(target) for target in prime_sums])

prob_sum_1 = simulate_dice_rolls(1)

# Print the probabilities
print("Probability of sum 7:", prob_sum_7)
print("Probability of prime sum:", prob_prime_sum)
print("Probability of sum 1:", prob_sum_1)
