#Import random (to generate random numbers) and Counter (to count how many times each value appears)
import random
from collections import Counter


#We fix the number of dices, we choose it to be 5 and we can modify it in the future if we want
DICE_COUNT = 5


#Defining the Header of the Game, we wanted it to be in a frame for an aesthetic purpose.
def print_header():
    print("╔══════════════════════════════════════════╗")
    print("║      🎲 DICE ROLLER SIMULATOR 🎲         ║")
    print("║      Roll 5 dice · Highest score wins    ║")
    print("╚══════════════════════════════════════════╝")


#Defining the Rules of the Game for the player. It shows how to play and the bonuses.
def print_rules():
    print()
    print("┌──────────────────────────────────────────┐")
    print("│               HOW TO PLAY                │")
    print("├──────────────────────────────────────────┤")
    print("│  1. Each player rolls 5 dices one by one │")
    print("│  2. Score = sum of dice × bonus          │")
    print("│  3. Highest score wins                   │")
    print("├──────────────────────────────────────────┤")
    print("│            BONUS MULTIPLIERS             │")
    print("├──────────────────────────────────────────┤")
    print("│  One pair          (e.g. 3 3 1 5 6)  ×2 │")
    print("│  Two pairs         (e.g. 3 3 5 5 1)  ×3 │")
    print("│  Three of a kind   (e.g. 4 4 4 2 6)  ×4 │")
    print("│  Full house        (e.g. 2 2 2 5 5)  ×5 │")
    print("│  Four of a kind    (e.g. 6 6 6 6 3)  ×6 │")
    print("│  Five of a kind    (e.g. 4 4 4 4 4)  ×8 │")
    print("│  Straight  (1-2-3-4-5 or 2-3-4-5-6) ×12 │")
    print("├──────────────────────────────────────────┤")
    print("│  Example: roll 3·3·5·5·2                 │")
    print("│  Two pairs → base 18 × 3 = 54 pts        │")
    print("└──────────────────────────────────────────┘")
    print()


#Defining the Roll Die function, picking a random intenger between 1 and 6
def roll_die():
    return random.randint(1, 6)


#Defining how we are showing the dices on the screen.
    #The highlight function will give some positions (the multipliers) in highlight. If nothing is given, we put an empty list.
    #The Parts function will create a new empty list to contain the dices.
    #We created a loop on the dices, i is the index and d is the value of the dice.
    #We decided to use the .join(parts) to assemble the elements with spaces.
def display_dice(dice, highlights=None):
    if highlights is None:
        highlights = []
    parts = []
    for i, d in enumerate(dice):
        parts.append(f"[{d}]" if i in highlights else f" {d} ")
    print("Dice:" + "  ".join(parts))


#Defining the analyze of the game. 
    #This analyze function will detect the combinaisons and return the multipliers, the bonus name and the highlight (multiplier, bonus_name, highlight_indices).
    #The counts will count how many times each value appears, the sorted_dice will detect the suites and the freqs will sort the number of counts in a descending order (from the strongest to the lowest).
def analyze(dice):
    counts = Counter(dice)
    sorted_dice = sorted(dice)
    freqs = sorted(counts.values(), reverse=True)

    #Straight: 1-2-3-4-5 or 2-3-4-5-6
    if sorted_dice in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
        return 12, "Straight!!!!!!!", list(range(DICE_COUNT))

    #Five of a kind: all the same elements 
    if freqs[0] == 5:
        val = [v for v, c in counts.items() if c == 5][0]
        idx = [i for i, d in enumerate(dice) if d == val]
        return 8, "Five of a kind!!!!!!", idx

    #Four of a kind: four same elements
    if freqs[0] == 4:
        val = [v for v, c in counts.items() if c == 4][0]
        idx = [i for i, d in enumerate(dice) if d == val]
        return 6, "Four of a kind!!!!", idx

    # Full house: exactly one triple + one pair (all the dice are useful so everything is highlighted)
    if freqs == [3, 2]:
        return 5, "Full house!!!!", list(range(DICE_COUNT))

    #Three of a kind: trhee items are identical
    if freqs[0] == 3:
        val = [v for v, c in counts.items() if c == 3][0]
        idx = [i for i, d in enumerate(dice) if d == val]
        return 4, "Three of a kind!!!", idx

    #Two pairs: some values appear two times
    pairs = [v for v, c in counts.items() if c == 2]
    if len(pairs) == 2:
        idx = [i for i, d in enumerate(dice) if d in pairs]
        return 3, "Two pairs!!", idx

    #One pair: two values are the same
    if len(pairs) == 1:
        idx = [i for i, d in enumerate(dice) if d == pairs[0]]
        return 2, "One pair!", idx

    #No bonus: nothing is the same, multiplier is 1 and nothing is highlighted
    return 1, "No bonus, damn...", []



#Defining how the game happens for a player.
    #We decided to frame the player's turn between horizontal lines. Name is the player's name and is_computer retruns true if it's the computer playing and false if it's an human.
def player_turn(name, is_computer=False):
    print(f"\n{'─' * 44}")
    print(f"  {'🤖' if is_computer else '👤'}  {name}'s turn")
    print(f"{'─' * 44}")

    #We initialise the dice list, by setting an emply list to store the 5 dice rolls
    dice = []

    #We roll the dice 5 times using a loop from 1 to 5 (because DICE_COUNT=5). 
        #The player sees that he needs to press to roll his dice or to watch the computer plays, we need to wait for his action.
        #The value calls the function defined before to give a random number between 1 to 6. 
        #The game then shows the value and stores it in the list.
    for i in range(1, DICE_COUNT + 1):
        input(f"  [Press Enter to {'watch ' + name + ' roll' if is_computer else 'roll'} die {i}/{DICE_COUNT}]")
        val = roll_die()
        print(f"  Die {i}: {val}")
        dice.append(val)

        #Analyse the final roll and compute the answer 
    multiplier, bonus, highlights = analyze(dice)
    base = sum(dice)
    final_score = base * multiplier

        #Shows the dice and highlight the important ones. We show the score.
    print()
    display_dice(dice, highlights)
    print()
    print(f"  Base score : {' + '.join(str(d) for d in dice)} = {base}")

        #Shows the bonus (if any)
    if multiplier > 1:
        print(f"  Bonus      : ✨✨ {bonus} (×{multiplier}) ✨✨")
        print(f"  Final score: {base} × {multiplier} = {final_score}")
    else:
        print(f"  Bonus      : {bonus}")
        print(f"  Final score: {final_score}")

        #Returns the final score
    return final_score


#Defining the scoreboard, showing the name of the player and their scores 
def print_scoreboard(player_names, scores):
    print(f"\n{'═' * 44}")
    print("  RESULTS")
    print(f"{'═' * 44}")
    for name, score in zip(player_names, scores):
        print(f"  {name:<25} {score} pts")
    print(f"{'─' * 44}")


#Defining the winner, we find the maximum score. If the scores are equal, there is no winner (tie)
def get_winner(player_names, scores):
    max_score = max(scores)
    winners = [name for name, score in zip(player_names, scores) if score == max_score]
    if len(winners) > 1:
        return None  # tie
    return winners[0]


#Defining the players, asking who is playing and decide if player 2 is human or computer. 
def setup_players():
    print()
    p1 = input("  Player 1 name [Player 1]: ").strip() or "Player 1"

    mode = input("  Player 2 — (h) Human or (c) Computer? [c]: ").strip().lower()
    is_computer = mode != "h"

    if is_computer:
        p2 = "Computer"
    else:
        p2 = input("  Player 2 name [Player 2]: ").strip() or "Player 2"

    return [p1, p2], [False, is_computer]



#Defining the main flow of the game. We display the header and the player must decide.
def play_game():
    print_header()

    
    #Ask if the player wants to read the rules first, and returns the rules.
    see_rules = input("\n  See the rules first? (y/n) [n]: ").strip().lower()
    if see_rules == "y":
        print_rules()
        input("  [Press Enter to continue to setup]")

    
    #Asking for the player's name, and returns to the defining players part.
    player_names, is_computer_list = setup_players()

    
    #Playing the game, we empty the list to store scores. We loop through the players turn, and each player plays a turn. The score is saved.
    scores = []
    for name, is_computer in zip(player_names, is_computer_list):
        score = player_turn(name, is_computer)
        scores.append(score)

    
    #Showing the scoreboard
    print_scoreboard(player_names, scores)

    
    #Determining the winner or the tie
    winner = get_winner(player_names, scores)
    if winner:
        print(f"  🏆  {winner} wins!")
    else:
        print("  🤝  It's a tie!")

    print(f"{'═' * 44}\n")

    
    #Asking to play again
    again = input("  Play again? (y/n) [n]: ").strip().lower()
    
        #If yes, we go back to the main page
    if again == "y":
        print("\n" + "=" * 44 + "\n")
        play_game()

        #If no, we display a message
    else:
        print("\n  Thanks for playing! 🎲\n")


#We want to have the game played directly without using another program, so we use this code as the program and we can reuse it if we want to make modifications. The game will start when we use the code.
if __name__ == "__main__":
    play_game()
