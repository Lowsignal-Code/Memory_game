# Memory Game

A simple terminal-based memory game written in Python. The goal is to memorize a sequence of numbers that grows longer each round and type it back correctly.

## How to Play

1. The program shows you a sequence of random numbers (between 1 and 9)
2. You get some time to memorize it (based on how long the sequence is)
3. The screen clears and you have to type the sequence back, separated by spaces
4. If you're correct, you move to the next round and a new number gets added to the sequence
5. If you're wrong, the game ends and shows you how far you got

## Requirements

- Python 3

No external libraries needed — just the standard `random` and `time` modules.

## How to Run

```bash
git clone https://github.com/HoneySpider/Memory_game.git
cd Memory_game
python Memory_game.py
```

## Project Structure

```
Memory_game/
├── Memory_game.py   # main game code
└── README.md
```

## Technical Note

The screen is cleared using `print("\033c", end="")`. This trick may not work in every environment (some IDEs or IDLE), so it's best to run it in a real terminal (CMD, PowerShell, or a Linux/macOS terminal).

## Project Status

⚠️ A small practice project for working with loops, conditionals, lists, and input/output in Python.

## Author

Made by **Lowsignal-Code**
