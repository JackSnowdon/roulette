import random
from collections import Counter

global slots

# Tradional Roulette Slots
slots = {
    "00": "green",
    "0": "green",
    "1": "red",
    "2": "black",
    "3": "red",
    "4": "black",
    "5": "red",
    "6": "black",
    "7": "red",
    "8": "black",
    "9": "red",
    "10": "black",
    "11": "red",
    "12": "black",
    "13": "red",
    "14": "black",
    "15": "red",
    "16": "black",
    "17": "red",
    "18": "black",
    "19": "red",
    "20": "black",
    "21": "red",
    "22": "black",
    "23": "red",
    "24": "black",
    "25": "red",
    "26": "black",
    "27": "red",
    "28": "black",
    "29": "red",
    "30": "black",
    "31": "red",
    "32": "black",
    "33": "red",
    "34": "black",
    "35": "red",
    "36": "black",
}


def spin(x):
    """
    Spins Roulette wheel a random number of times
    Returns winning slot and fills results
    for all slots landed on

    paramater: int for how many spins
    """
    amount_of_slots = len(slots)

    # Randomly sets spin_counter using randint
    global spin_counter
    spin_counter = random.randint(1 + x, amount_of_slots + x)

    # Spins amount of times and adds winner to results list
    for spin in range(1, spin_counter + 1):
        winner = random.choice(list(slots.keys()))
        results.append(winner)
        """
        Prints out every winner
        print("Spin: {0} - {1} {2}".format(spin, winner, slots[winner].capitalize()))
        """
    print("Spin {0}: - {1} {2}".format(spin,
    winner, slots[winner].capitalize()))
    print("WINNER: {0} {1}".format(winner, slots[winner].capitalize()))
    # print(f"Amount of Spins: {spin_counter}")
    return winner


def getMostCommonNumbers():
    """
    Using Counter on the most recent results to itarate
    over winning numbers. Populates "most_commmon_numbers" with
    results or they can be returned
    """

    # Counter used with results to create a useable dataset
    counter = Counter(results)

    """
    Top one result
    most_common_slot = counter.most_common(1)
    print(f"Most Common Number: {most_common_slot}")

    Gets top_three most common winners
    top_three = counter.most_common(3)
    print(f"Top Three Numbers: {top_three}")
    """

    # Grabs top third of most common countered numbers

    top_segment = counter.most_common(int(spin_counter / 3))
    top_result = top_segment[0]

    for t in top_segment:
        # Breaks down top segment into key value pairs
        number = t[0]
        hits = t[1]

        # The first instance will always pass the if loop
        # Allowing a benchmark to be set for the remaining instances
        if hits >= top_result[1]:
            most_common_numbers.append(number)
        else:
            break

    count = 0

    for n in most_common_numbers:
        most_common_numbers[count] = str(n) + " " + getColor(n)
        count += 1

    if len(most_common_numbers) == 1:
        print(f"Most Common Number Is: {most_common_numbers[0]} with {hits} instances")
    else:
        numlist = ", ".join(most_common_numbers)
        print(f"Most Common Numbers Are: {numlist} with {hits} instances")

    return most_common_numbers


def getColor(x):
    """
    Returns color value of int from slots

    parameters: int
    """
    return slots[x].capitalize()


def getUserChoice():
    """
    Uses input to obtain user choice

    Returns capitaliszed if str (color choice)
    or as an in (number choice)
    """

    color_choices = {"red", "black", "green"}
    number_choices = list(slots.keys())

    choice = input("Pick a number between 00-36, or red, black or green?: ")
    print("")

    if choice not in color_choices and choice not in number_choices:
        print("Invalid Input, try again: ")
        return getUserChoice()
    else:
        if choice in color_choices:
            return choice.capitalize()
        else:
            return int(choice)


def placeBet():
    """
    Returns int of amount of coints bet
    """
    print(f"Coins: {user.coins}")
    amount = int(input("How much do you want to bet?: "))
    if amount <= user.coins:
        user.coins -= amount
        print(f"{amount} coins bet on {choice}")
        return amount
    else:
        print("You dont have enough coins")
        return placeBet()


def checkWinner(choice, bet):
    """
    Checks user input guess and sets winnings
    first parameter is set via getUserChoice
    and type will decide flow

    parameters: choice(int/str), bet(int)
    """
    if type(choice) == str:
        if getColor(winner) == choice:
            winnings = bet * 2
            user.coins += winnings
            print(f"You Win {winnings} Coins")
        else:
            print("You Lose!")
    else:
        print(winner, choice)
        if int(winner) == choice:
            winnings = bet * 10
            user.coins += winnings
            print(f"You Win {winnings} Coins")
        else:
            print("You Lose!")
    print(f"Coins left: {user.coins}")


def checkIfBroke(c):
    """
    Checks if user coins is 0
    """
    if c == 0:
        return True


class Player:
    coins = 100


user = Player()
running = True


while running == True:
    results = []
    most_common_numbers = []

    choice = getUserChoice()
    bet = placeBet()
    winner = spin(10)

    print("")
    checkWinner(choice, bet)
    print("")

    if checkIfBroke(user.coins):
        running = False
        print("You're broke, Game Over!")
        break

    repeat = input("Press Any Key to play again, or type q to leave: ")

    if repeat == "q":
        running = False
