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

- The solver will make random guesses when no logical moves are available.

---

## 📦 Requirements

- Python 3.6+
- Pygame

Install Pygame using:

```bash
pip install pygame
```

**Note**: On macOS and some Linux systems, you may need to use `python3` instead of `python`:

```bash
python3 -m pip install pygame
```

---

## 🗂️ Required Assets

Make sure you have these folders and files in your project directory:

```text
minesweeper/
├── images/
│   ├── empty-block.png
│   ├── flag.png
│   ├── bomb-at-clicked-block.png
│   ├── unclicked-bomb.png
│   ├── wrong-flag.png
│   ├── 0.png
│   ├── 1.png
│   ├── 2.png
│   ├── ... (up to 8.png)
├── sounds/
│   ├── win.wav           # Win sound effect
│   ├── lose.wav          # Lose sound effect
```

---

## ▶️ Run the Game

Run the program from your terminal:

```bash
python main.py
```

**For macOS/Linux users:**
```bash
python3 main.py
```

---

## 🏃 Run with Shell Script

Alternatively, run the game with:

```bash
./run.sh
```

---

## 🗂️ Project Structure

```text
minesweeper/
├── main.py           # Entry point with menu interface and game launch
├── game.py           # Game logic, Pygame rendering, and main game loop
├── board.py          # Board management and game state logic
├── piece.py          # Individual game piece class
├── solver.py         # Enhanced AI solver with advanced logic
├── images/           # PNG images for all game pieces (required)
├── win.wav           # Win sound effect (required)
├── lose.wav          # Lose sound effect (optional)
└── README.md         # This file
```

---

## 🎯 Game Features

- **Three Difficulty Levels**: Easy (10x10, 10 mines), Medium (16x16, 40 mines), Hard (20x20, 80 mines)
- **Manual or AI Play**: Choose to play yourself or watch the AI solve
- **Smart AI Solver**: Think logically and makes random guesses when needed
- **Visual Feedback**: Bomb counter and win/lose messages
