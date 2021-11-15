"""
    Question 1:
    Alice has some cards with numbers written on them, she arranges the cards in decreasing order and lays
    them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
    number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""
# testcases/edge cases
tests = [
    {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3},
    {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6},
    {"input": {"cards": [4, 13, 11, 10, -1], "query": 4}, "output": 3},
    {"input": {"cards": [6], "query": 6}, "output": 0},
    {"input": {"cards": [], "query": 7}, "output": -1},
    {
        "input": {"cards": [13, 11, 10, 10, 10, 10, 7, 4, 3, 1, 0], "query": 10},
        "output": 2,
    },
]

# SOLVING WITH LINEAR SEARCH
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        # check if element at current position match the query
        if cards[position] == query:
            return position
        position += 1
    return -1


def _test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


# optimized solution
# SOLVE WITH BINARY SEARCH
def locate_card_binary(cards: list, query: int):
    cards = sorted(cards, reverse=True)
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        result = _test_location(cards, query, mid)

        if result == "found":
            return mid

        elif result == "left":
            high = mid - 1

        elif result == "right":
            low = mid + 1

    return -1


# tests_v2 = [{"input": {"cards": [4, 13, 11, 10, -1], "query": 4}, "output": 3}]
# for test in tests:
#     response = locate_card_v2(**test["input"]) == test["output"]
#     print("version_2", response)


"""
    Question 2. 
    Find the first and last position of an element in a sorted array.
    Example given an array of intergers numbers sorted in ascending order, find the 
    starting and ending position of a given target.

    Example. numbers = [5, 7, 7, 8, 8, 10] target = 8, output= [3, 4[]
    If target not found return [-1, -1]
"""

# 2 - Test scenarios for some edge cases that we will want to cover
tests_data = [
    {
        "input": {"numbers": [13, 11, 10, 7, 7, 4, 3, 1, 0], "target_number": 7},
        "output": [4, 5],
    },  # not properly sorted
    {
        "input": {
            "numbers": [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 9],
            "target_number": 8,
        },
        "output": [8, 9],
    },  # perfect scenario
    {"input": {"numbers": [], "target_number": 8}, "output": [-1, -1]},  # empty list
    {
        "input": {
            "numbers": [1, 1, 3, 5, 6, 8],
            "target_number": 1,
        },
        "output": [0, 1],
    },  # When the number occurs at the first and second position
    {
        "input": {
            "numbers": [1, 2, 3, 4, 5, 5, 9, 9, 9],
            "target_number": 9,
        },
        "output": [6, 8],
    },  # when the number occur at the end part of the array
    {
        "input": {
            "numbers": [11, 22, 13, 44, 55, 25, 86, 77, 38, 98, 98, 78, 9],
            "target_number": 98,
        },
        "output": [11, 12],
    },  # perfect scenario
]


# Solving with linear search
def locate_first_and_last_position_of_element_linear(
    numbers: list, target_number: int
) -> list[int, int]:
    # sort the array in ascending order
    items = sorted(numbers)
    # print({"sorted_array": items})

    initial_position = 0

    # This will take care of the edge case if no item is inside the array
    if len(items) == 0:
        return [-1, -1]

    result: list = []

    while len(items) > initial_position:

        # print(items[initial_position], "is at index ", initial_position)

        if items[initial_position] == target_number:
            # print(initial_position, "initial position")
            result.append(initial_position)

        initial_position += 1

    first = result[0]
    last = result[-1]
    return [first, last]


# Solving with binary search
def locate_first_and_last_position_of_element_binary(
    numbers: list, target_number: int
) -> list[int, int]:

    numbers = sorted(numbers)
    l, r = 0, len(numbers) - 1
    while l <= r:
        mid = (l + r) // 2
        # If the mid number matches target_number, search neighbors until mismatch
        if numbers[mid] == target_number:
            start, end = mid, mid

            while start > l and numbers[start - 1] == target_number:
                start -= 1

            while end < r and numbers[end + 1] == target_number:
                end += 1
            return [start, end]
        elif numbers[mid] < target_number:
            l = mid + 1
        else:
            r = mid - 1

    return [-1, -1]


# for test in tests_data:
#     response = locate_first_and_last_position_of_element_binary(**test["input"])
#     check = response == test["output"]
#     print(check)


"""
    Question 3
    You are given list of numbers, obtained by rotating a sorted list an unknown
    number of times. Write a function to determine the minimum number of times the
    original sorted list was rotated to obtain the given list. Your function should have
    the worst-case complexity of O(log N), where N is the length of the list. You can
    assume that all the numbers in the list are unique.
    Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the
    sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
    We define "rotating a list" as removing the last element of the list and adding it
    before the first element. E.g. rotating the list [3, 2, 4,
    11 produces [1, 3,
    2, 4].
    "Sorted list" refers to a list where the elements are arranged in the increasing order
    e.g. [1, 3, 5, 7].
"""

# Solved with linear search
def count_rotations_linear(numbers):
    size = len(numbers)

    if size == 0:
        return 0

    # finf the index of the minimum element
    min_element = numbers[0]

    for i in range(0, size):
        if min_element > numbers[i]:
            min_element = numbers[i]
            min_index = i

    return min_index


# response = count_rotations_linear([5, 6, 9, 0, 2, 3, 4])
# print(response)

# solved with binary search
def count_rotations(arr):
    n = len(arr)
    start = 0
    end = n - 1
    # finding the index of minimum of the array
    # index of min would be equal to number to rotation
    while start <= end:

        # middle number
        mid = start + (end - start) // 2

        if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
            new_array = arr[:mid]
            return len(new_array)

        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            new_array = arr[: mid + 1]
            return len(new_array)


# response = count_rotations([5, 6, 9, 10, 13, 0, 2, 3, 4])
# print(response, "this is the response")


"""
    Question 4 
    Find Minimum in Rotated Sorted Array
"""


def find_min(nums):
    # If the list has just one element then return that element.
    if len(nums) == 1:
        return nums[0]

    # left pointer
    left = 0
    # right pointer
    right = len(nums) - 1

    # if the last element is greater than the first element then there is no rotation.
    # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
    # Hence the smallest element is first element. A[0]
    if nums[right] > nums[0]:
        return nums[0]

    # Binary search way
    while right >= left:
        # Find the mid element
        mid = left + (right - left) // 2

        # if the mid element is greater than its next element then mid+1 element is the smallest
        # This point would be the point of change. From higher to lower value.
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # if the mid element is lesser than its previous element then mid element is the smallest
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # if the mid elements value is greater than the 0th element this means
        # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
        if nums[mid] > nums[0]:
            left = mid + 1
        # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
        else:
            right = mid - 1
