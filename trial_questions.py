"""
Question
    You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds'
    scores.
    At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record
    and is one of the following:
    An integer x - Record a new score of x
    "+" - Record a new score that is the sum of the previous two scores. It is quaranteed there will always be two previous scores.
    "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
    "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score
    Return the sum of all the scores on the record.
"""

# solution

# def sum_of_scores_on_a_board(array: List) -> int

tests_data = [
    {
        "input": {"array": ["5", "2", "C", "D", "+"]},
        "output": 30,
    },  # not properly sorted
    {
        "input": {"array": ["5", "-2", "4", "C", "D", "9", "+", "+"]},
        "output": 27,
    },
    {
        "input": {"array": ["1"]},
        "output": 1,
    },
]


def sum_of_scores_on_a_board(array: list) -> int:
    record = []

    for i in array:
        if i.isdigit() or "-" in i:
            record.append(int(i))
        elif i == "+":
            score = record[-1] + record[-2]
            record.append(score)
        elif i == "D":
            score = record[-1] * 2
            record.append(score)
        elif i == "C":
            record.pop()
    total_records = sum(record)
    return total_records


for test in tests_data:
    result = sum_of_scores_on_a_board(**test["input"])
    print(result == test["output"])
