# Import the images
from H_L_art import logo, vs
from H_L_game_data import data
import random


def clear():
    print('\n' * 50)

# Providing the comparing options that are randomly selected.
def compare(random_data1, random_data2):
    print(f"Compare A: {random_data1['name']}, {random_data1['description']}, "
          f"from {random_data1['country']}")
    print(vs)
    print(f"Against B: {random_data2['name']}, {random_data2['description']}, "
          f"from {random_data2['country']}")

def conditions(score, winning, random_data1, random_data2):
    # Winning conditions
    followers = input("Who has more followers? Type 'A' or 'B':").upper()

    if followers == 'A' and random_data1['follower_count'] > random_data2['follower_count']:
        return winning, followers

    elif followers == 'B' and random_data1['follower_count'] < random_data2['follower_count']:
        return winning, followers

    # Losing conditions
    elif followers == 'B' and random_data1['follower_count'] > random_data2['follower_count']:
        winning = False
        return winning, followers

    elif followers == 'A' and random_data1['follower_count'] < random_data2['follower_count']:
        winning = False
        return winning, followers


def game():
    print(logo)
    score = 0
    winning = True
    random_data1 = random.choice(data)
    random_data2 = random.choice(data)
    try:
        while winning:
            random_data1 = random_data2
            random_data2 = random.choice(data)
            while random_data2 == random_data1:
                random_data2 = random.choice(data)
            compare(random_data1, random_data2)
            win, followers = conditions(score, winning, random_data1, random_data2)

            if win == True:
                score += 1
                clear()
                print(f"You're right! Current score: {score}")
            else:
                # clear()
                print(f"Sorry, that's wrong. Final score: {score}")
                score = 0
                winning = False

                play_again = int(input("Would you like to play again, Type 0 for 'NO' and Type 1 for 'YES'"))
                if play_again == 1:
                    clear()
                    game()
    except TypeError:
        game()
game()



