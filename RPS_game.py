import random

def play(player1, player2, num_games=1000, verbose=False):
    p1_wins = 0
    p2_wins = 0
    ties = 0

    p1_prev = ""
    p2_prev = ""

    for _ in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if verbose:
            print(f"Player 1: {p1_move} | Player 2: {p2_move}")

        if p1_move == p2_move:
            ties += 1
        elif (p1_move == "R" and p2_move == "S") or \
             (p1_move == "P" and p2_move == "R") or \
             (p1_move == "S" and p2_move == "P"):
            p1_wins += 1
        else:
            p2_wins += 1

        p1_prev = p1_move
        p2_prev = p2_move

    total = p1_wins + p2_wins + ties
    print(f"Player 1 won {p1_wins} times ({(p1_wins/total)*100:.2f}%)")
    print(f"Player 2 won {p2_wins} times ({(p2_wins/total)*100:.2f}%)")
    print(f"Ties: {ties} times ({(ties/total)*100:.2f}%)")


# Opponent: Quincy – repeats a fixed pattern
def quincy(prev_play, pattern=["R", "P", "S", "R", "P", "S"]):
    if not hasattr(quincy, "index"):
        quincy.index = 0
    play = pattern[quincy.index % len(pattern)]
    quincy.index += 1
    return play


# Opponent: Abbey – uses frequency analysis
def abbey(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return "R"

    from collections import Counter
    counter = Counter(opponent_history)
    most_common = counter.most_common(1)[0][0]

    def beat(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    return beat(most_common)


# Opponent: Kris – chooses based on what you just played
def kris(prev_play):
    if prev_play == "":
        return "R"
    return prev_play


# Opponent: Mrugesh – predicts your most common move and counters it
def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    from collections import Counter
    guess = Counter(opponent_history).most_common(1)[0][0]

    def beat(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    return beat(guess)
