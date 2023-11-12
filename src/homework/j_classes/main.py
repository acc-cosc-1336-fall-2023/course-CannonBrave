from class_a import Die
import time

while True:
    die = Die()
    die.roll()
    print(die)

    continue_playing = input('Roll again? (y/n): ')
    if continue_playing != "y":
        break
