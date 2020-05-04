import random
from collections import Counter

global slots

# Tradional Roulette Slots 
slots = {'00': 'green', '0': 'green', '1': 'red', '2': 'black',
         '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
         '8': 'black', '9': 'red', '10': 'black', '11': 'red',
         '12': 'black', '13': 'red', '14': 'black', '15': 'red',
         '16': 'black', '17': 'red', '18': 'black', '19': 'red',
         '20': 'black', '21': 'red', '22': 'black', '23': 'red',
         '24': 'black', '25': 'red', '26': 'black', '27': 'red',
         '28': 'black', '29': 'red', '30': 'black', '31': 'red',
         '32': 'black', '33': 'red', '34': 'black', '35': 'red',
         '36': 'black'}

results = []

def spin(x):
    """
    Spins Roulette wheel a random number of times
    Returns winning slot but also fills results 
    for all slots landed on

    paramater: int for how many spins
    """
    amount_of_slots = len(slots)

    # Randomly sets spin_counter using randint
    global spin_counter
    spin_counter = random.randint(1, amount_of_slots + x)

    # Spins amount of times and adds winner to results list
    for spin in range(1, spin_counter + 1):      
        winner = random.choice(list(slots.keys()))
        results.append(winner)
        """
        Prints out every winner 
        print("Spin: {0} - {1} {2}".format(spin, winner, slots[winner].capitalize()))
        """
    return winner

winner = spin(10)

print("WINNER: {0} {1}".format(winner, slots[winner].capitalize()))
print(f"Amount of spins: {spin_counter}")


counter = Counter(results)
most_common_slot = counter.most_common(1)
top_three = counter.most_common(3)
print(f"Most Common Number: {most_common_slot}")
print(f"Top Three Numbers: {top_three}")
