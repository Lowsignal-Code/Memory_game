import random
import time

def play_game():
    sequence = []
    round_number = 0

    print("=== Memory Game ===")
    print("I'll show you a sequence of numbers, you have to type them back in order!\n")

    while True:
        round_number += 1
        sequence.append(random.randint(1, 9))

        print(f"--- Round {round_number} ---")
        print("Memorize this sequence:")
        print(" ".join(str(n) for n in sequence))
        time.sleep(len(sequence) * 0.8 + 1)
        print("\033c", end="")  # clear the screen

        answer = input("Now type the sequence separated by spaces: ").split()

        try:
            answer = [int(x) for x in answer]
        except ValueError:
            answer = []

        if answer == sequence:
            print(f" Correct! Moving on to round {round_number + 1}\n")
        else:
            print(f" Wrong! The correct sequence was: {' '.join(str(n) for n in sequence)}")
            print(f"You made it to round {round_number}.")
            break

if __name__ == "__main__":
    play_game()