import random
from collections import Counter

# ─────────────────────────────────────────────────────────────
#  DICE ROLLER SIMULATOR
#
#  Rules:
#    - Each player rolls 5 dices, one at a time
#    - Score = sum of all dices × bonus multiplier
#    - Highest score wins
#
#  Bonus multipliers:
#    One pair          ×2
#    Two pairs         ×3
#    Three of a kind   ×4
#    Full house (3+2)  ×5
#    Four of a kind    ×6
#    Five of a kind    ×8
#    Straight          ×12
# ─────────────────────────────────────────────────────────────

DICE_COUNT = 5


def print_header():
    print("╔══════════════════════════════════════════╗")
    print("║        🎲  DICE ROLLER SIMULATOR 🎲      ║")
    print("║    Roll 5 dice · Highest score wins      ║")
    print("╚══════════════════════════════════════════╝")


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


def roll_die():
    return random.randint(1, 6)


def display_dice(dice, highlights=None):
    """
    Print dice values. Highlighted dice (forming a bonus)
    are shown in [brackets], others without.
    """
    if highlights is None:
        highlights = []
    parts = []
    for i, d in enumerate(dice):
        parts.append(f"[{d}]" if i in highlights else f" {d} ")
    print("  Dice: " + "  ".join(parts))


def analyze(dice):
    """
    Analyze dice and return (multiplier, bonus_name, highlight_indices).
    """
    counts = Counter(dice)
    sorted_dice = sorted(dice)
    freqs = sorted(counts.values(), reverse=True)

    # Straight: 1-2-3-4-5 or 2-3-4-5-6
    if sorted_dice in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
        return 12, "Straight!!!!!!!", list(range(DICE_COUNT))

    if freqs[0] == 5:
        val = [v for v, c in counts.items() if c == 5][0]
        idx = [i for i, d in enumerate(dice) if d == val]
        return 8, "Five of a kind!!!!!!", idx

    if freqs[0] == 4:
        val = [v for v, c in counts.items() if c == 4][0]
        idx = [i for i, d in enumerate(dice) if d == val]
        return 6, "Four of a kind!!!!", idx

    # Full house: exactly one triple + one pair
    if freqs == [3, 2]:
        return 5, "Full house!!!!", list(range(DICE_COUNT))

    if freqs[0] == 3:
        val = [v for v, c in counts.items() if c == 3][0]
        idx = [i for i, d in enumerate(dice) if d == val]
        return 4, "Three of a kind!!!", idx

    pairs = [v for v, c in counts.items() if c == 2]
    if len(pairs) == 2:
        idx = [i for i, d in enumerate(dice) if d in pairs]
        return 3, "Two pairs!!", idx

    if len(pairs) == 1:
        idx = [i for i, d in enumerate(dice) if d == pairs[0]]
        return 2, "One pair!", idx

    return 1, "No bonus, damn...", []


def player_turn(name, is_computer=False):
    """
    Run one full turn: roll 5 dice one at a time, compute and return score.
    """
    print(f"\n{'─' * 44}")
    print(f"  {'🤖' if is_computer else '👤'}  {name}'s turn")
    print(f"{'─' * 44}")

    dice = []

    for i in range(1, DICE_COUNT + 1):
        input(f"  [Press Enter to {'watch ' + name + ' roll' if is_computer else 'roll'} die {i}/{DICE_COUNT}]")
        val = roll_die()
        print(f"  Die {i}: {val}")
        dice.append(val)

    # Analyse the final roll
    multiplier, bonus, highlights = analyze(dice)
    base = sum(dice)
    final_score = base * multiplier

    print()
    display_dice(dice, highlights)
    print()
    print(f"  Base score : {' + '.join(str(d) for d in dice)} = {base}")

    if multiplier > 1:
        print(f"  Bonus      : ✨ {bonus} (×{multiplier})")
        print(f"  Final score: {base} × {multiplier} = {final_score}")
    else:
        print(f"  Bonus      : {bonus}")
        print(f"  Final score: {final_score}")

    return final_score


def print_scoreboard(player_names, scores):
    print(f"\n{'═' * 44}")
    print("  RESULTS")
    print(f"{'═' * 44}")
    for name, score in zip(player_names, scores):
        print(f"  {name:<25} {score} pts")
    print(f"{'─' * 44}")


def get_winner(player_names, scores):
    max_score = max(scores)
    winners = [name for name, score in zip(player_names, scores) if score == max_score]
    if len(winners) > 1:
        return None  # tie
    return winners[0]


def setup_players():
    """
    Ask for player names and game mode.
    Returns (player_names, is_computer_list).
    """
    print()
    p1 = input("  Player 1 name [Player 1]: ").strip() or "Player 1"

    mode = input("  Player 2 — (h) Human or (c) Computer? [c]: ").strip().lower()
    is_computer = mode != "h"

    if is_computer:
        p2 = "Computer"
    else:
        p2 = input("  Player 2 name [Player 2]: ").strip() or "Player 2"

    return [p1, p2], [False, is_computer]


def play_game():
    print_header()

    # Ask if they want to read the rules first
    see_rules = input("\n  See the rules first? (y/n) [n]: ").strip().lower()
    if see_rules == "y":
        print_rules()
        input("  [Press Enter to continue to setup]")

    # Setup players
    player_names, is_computer_list = setup_players()

    # Play each turn
    scores = []
    for name, is_computer in zip(player_names, is_computer_list):
        score = player_turn(name, is_computer)
        scores.append(score)

    # Results
    print_scoreboard(player_names, scores)

    winner = get_winner(player_names, scores)
    if winner:
        print(f"  🏆  {winner} wins!")
    else:
        print("  🤝  It's a tie!")

    print(f"{'═' * 44}\n")

    # Play again?
    again = input("  Play again? (y/n) [n]: ").strip().lower()
    if again == "y":
        print("\n" + "=" * 44 + "\n")
        play_game()
    else:
        print("\n  Thanks for playing! 🎲\n")


if __name__ == "__main__":
    play_game()
