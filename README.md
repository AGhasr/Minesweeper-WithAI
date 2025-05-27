# 🕹️ Minesweeper with AI Solver

A Minesweeper game built with Pygame featuring an optional AI solver that can play the game for you!

---

## 🎮 How to Play

- Choose the difficulty level at the start (Easy, Medium, Hard).
- Choose whether to play manually or let the AI solver play.
- If you choose AI mode, **you need to click the first tile manually** to initialize the board before the AI starts.
- The AI will then try to solve the board automatically.

---

## ⚠️ Important Notes about the AI Solver

- The AI uses basic Minesweeper logic to flag bombs and reveal safe tiles.
- Sometimes the AI may get stuck if it cannot deduce a safe move, just like a human might.
- In that case, the AI will stop making moves, and the game will wait for your input.

---

## 📦 Requirements

- Python 3.6+
- Pygame

Install Pygame using:

```bash
pip install pygame
```

## ▶️ Run the Game

Run the program from your terminal:

```bash
python gravity_simulator.py
```

## 🏃 Run with Shell Script

Alternatively, run the game with:

```bash
./run.sh
```
🗂️ Project Structure
```text
minesweeper/
├── main.py           # Entry point with interface and game launch
├── game.py           # Game logic and Pygame loop
├── board.py          # Board and piece classes
├── solver.py         # AI solver logic
├── piece.py          # Game piece class
├── images/           # Images used in the game (flags, bombs, numbers)
├── sounds/           # The sounds used in the game
└── README.md         # This file