# DiceRollerSimulator

## How to play

Each player rolls **5 dice**, one at a time. Your score is the sum of all dice multiplied by a bonus depending on what you rolled. The player with the highest score wins.

## Bonus multipliers

| Hand | Example | Multiplier |
|---|---|---|
| One pair | 3 3 1 5 6 | ×2 |
| Two pairs | 3 3 5 5 1 | ×3 |
| Three of a kind | 4 4 4 2 6 | ×4 |
| Full house | 2 2 2 5 5 | ×5 |
| Four of a kind | 6 6 6 6 3 | ×6 |
| Five of a kind | 4 4 4 4 4 | ×8 |
| Straight | 1 2 3 4 5 or 2 3 4 5 6 | ×12 |

**Example:** you roll 3 · 3 · 5 · 5 · 2 → two pairs → base score 18 × 3 = **54 pts**

## Play the game

**In the browser — no install needed**
Open `dice_roller.html` in any browser (Chrome, Firefox, Safari). Just double-click the file or use the GitHub Pages link.

**In the terminal — requires Python 3**
```bash
python dice_roller.py
```

## Game modes

- **Human vs Computer** — play against the CPU (default)
- **Human vs Human** — pass the keyboard to a friend

