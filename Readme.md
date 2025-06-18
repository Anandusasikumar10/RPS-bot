# Rock Paper Scissors Bot 🤖✊✋✌️

This project implements a smart bot that plays Rock, Paper, Scissors using **pattern recognition** and **adaptive strategy**. It competes against four different bots and must win more than **60% of the games** in each match.

## 🧠 Strategy

- Tracks the opponent’s last 3 moves (n-gram model)
- Predicts the next move based on past patterns
- Counters that move to win

## 📁 Files

- `RPS.py`: Your intelligent player bot
- `RPS_game.py`: Game engine and opponents (`quincy`, `abbey`, `kris`, `mrugesh`)
- `main.py`: Script to test your player against opponents
- `test_module.py`: (Optional) Tests for verifying accuracy

## ▶️ How to Run

```bash
python main.py
