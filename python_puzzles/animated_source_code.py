import time
import os


def typing_animation(text, delay=0.005):
    for char in text:
        print(char, end="", flush=True)  # Print each character without newline
        time.sleep(delay)
    print()  # Print a newline after animation is done


home_folder = os.path.expanduser("~")
# input_text = input("Enter a text: ")
with open(
    f"{home_folder}/Development/python_puzzles/python_puzzles/split_deck.py"
) as file:
    input_text = file.read()
typing_animation(input_text)
