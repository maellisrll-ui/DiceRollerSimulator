# DiceRollerSimulator 🎲

Welcome to our group's game ! We are happy to show you our work for the Python class. We've coded a dice roller simulator that enables you to play against your friend or against the computer. The objective is to roll 5 dices and to make the highest score. 
Good luck and have fun !!

🩷 By Jefferson, Malika, Ahmad, Walid, Larissa, and Maëllis 🩷




## How to play 🎲

Each player rolls **5 dice**, one at a time. 

Your score is the sum of all dice. 

This score can be multiplied by a bonus depending on what you rolled. 

The player with the highest score wins.




## Bonus multipliers 🎲

| Hand | Example | Multiplier |
|---|---|---|
| One pair | 3 3 1 5 6 | ×2 |
| Two pairs | 3 3 5 5 1 | ×3 |
| Three of a kind | 4 4 4 2 6 | ×4 |
| Full house | 2 2 2 5 5 | ×5 |
| Four of a kind | 6 6 6 6 3 | ×6 |
| Five of a kind | 4 4 4 4 4 | ×8 |
| Straight | 1 2 3 4 5 or 2 3 4 5 6 | ×12 |

### Scores Examples 🎲

**Example:** you roll 1 · 2 · 3 · 3 · 4 → one pair → base score 13 × 2 = **26 pts**

**Example:** you roll 3 · 3 · 5 · 5 · 2 → two pairs → base score 18 × 3 = **54 pts**

**Example:** you roll 3 · 3 · 3 · 5 · 5 → Full house → base score 19 × 5 = **95 pts**

The **lowest score** happens when you roll 1 · 1 · 2 · 3 · 4 → one pair → base score 11 × 2 = **22 pts**

The **highest score** happens when you roll 2 · 3 · 4 · 5 · 6 → Straight → base score 20 × 12 = **240 pts** 




## Play the game 🎲

**In the browser : no install needed**


Open `dice_roller.html` in any browser (Chrome, Firefox, Safari). 

Just double-click the file or use the GitHub Pages link.


**In the terminal : requires Python 3**

```bash
python dice_roller.py
```


## Game modes 🎲

We have decided on two modes, you can either play against your computer, or against your friends.
Future modes of the game include an online version that enables you to play against foreigner at the other corner of the World.

- **Human vs Computer** : play against the CPU (default) 🤖
- **Human vs Human** : pass the keyboard to a friend 🧠

