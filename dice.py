from random import randint

# function to roll a d-sided die n times 
def roll(n, d):
    total = 0
    for i in range(n):
        total = total + randint(1,d)
    return total

# function to tally n rolls of a d-sided die
def countRolls(n, d):
    freq = [0] * (d+1)
    for i in range(n):
        j = randint(1,d)
        freq[j] += 1
    return freq
