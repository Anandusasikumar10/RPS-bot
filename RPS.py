import random

def player(prev_play, opponent_history=[], play_order={}):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 4:
        return random.choice(["R", "P", "S"])

    last_three = "".join(opponent_history[-3:])

    if last_three not in play_order:
        play_order[last_three] = {"R": 0, "P": 0, "S": 0}

    if len(opponent_history) >= 4:
        prev_seq = "".join(opponent_history[-4:-1])
        next_move = opponent_history[-1]
        if prev_seq not in play_order:
            play_order[prev_seq] = {"R": 0, "P": 0, "S": 0}
        play_order[prev_seq][next_move] += 1

    prediction = max(play_order[last_three], key=play_order[last_three].get)

    def beat(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    return beat(prediction)
