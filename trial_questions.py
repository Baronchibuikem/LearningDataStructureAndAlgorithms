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
        # if i.isdigit() or "-" in i:
        #     record.append(int(i))
        if i == "+":
            score = record[-1] + record[-2]
            record.append(score)
        elif i == "D":
            score = record[-1] * 2
            record.append(score)
        elif i == "C":
            record.pop()
        else:
            record.append(int(i))

    total_records = sum(record)
    return total_records


# for test in tests_data:
#     result = sum_of_scores_on_a_board(**test["input"])
#     print(result == test["output"])


"""
    Question.
    Given an array of integers, return indices of the two numbers such that they add up to a 
    specific target.

    You may assume that each input would have exactly one solution and you may not use the same element 
    twice
"""

# Solution
# Given an array, get the indexes of the two elements that will add to the given target

# inputs = [2, 7, 11, 16], target_number = 9
# output = [0,1]

# function scalford = def find_indexes(items:list, sum:int) -> list[int]

# edge cases:
#  empty list
#  correct numbers occuring at the end of the array
#  correct number occuring at the middle of the array
#  correct number occuring at the end of the array
#  correct indexs not found

test_data = [
    {"inputs": {"items": [], "summed": 9}, "output": [-1, -1]},
    {"inputs": {"items": [2, 7, 11, 16], "summed": 9}, "output": [0, 1]},
    {
        "inputs": {"items": [8, 12, 13, 82, 40, 7, 11, 16, 24], "summed": 40},
        "output": [5, 6],
    },
    {"inputs": {"items": [8], "summed": 9}, "output": [-1, -1]},
    {
        "inputs": {"items": [8, 12, 13, 82, 40, 7, 11, 16, 24], "summed": 19},
        "output": [1, 2],
    },
]


def find_index(items: list, summed: int) -> list[int]:
    # sort the list
    sorted_items = sorted(items)

    if len(sorted_items) == 0 or len(sorted_items) == 1:
        return [-1, -1]

    for i in range(0, len(sorted_items) - 1):
        if sorted_items[i] + sorted_items[i + 1] == summed:
            return [
                sorted_items.index(sorted_items[i]),
                sorted_items.index(sorted_items[i + 1]),
            ]

        continue


def find_index2(items: list, summed: int) -> list(int):

    sorted_items = sorted(items)
    left, right = 0, len(sorted_items) - 1

    while right > left:
        mid_point = (left + right) // 2
        print(mid_point)

        if sorted_items[mid_point] + sorted_items[mid_point - 1] > summed:
            return [
                sorted_items.index(sorted_items[mid_point]),
                sorted_items.index(sorted_items[mid_point + -1]),
            ]
        else:
            left -= 1


# for test in test_data:
#     result = find_index(**test["inputs"])
#     print("<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")
#     print(result == test["output"])


"""
    Question
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
"""

"""Write a function to create a balanced BST from a sorted list/array of key-value pairs"""
