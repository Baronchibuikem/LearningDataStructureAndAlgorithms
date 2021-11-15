from answers_to_questions_on_sorting import SortAnswers

sort_manager = SortAnswers()


# QUESTION 1

# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it
# In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

# Example 1:

# Input:
# n = 5
# arr[] = {1,2,3,4,5}
# Output: 2 1 4 3 5
# Explanation: Array elements after 
# sorting it in wave form are 
# 2 1 4 3 5.

# complete the function below
# def convertToWave(array, n):
    #Your code here

    # to see a working solution comment out the response, print, sample_wave_array_data and convertToWave below
    # response: list[int] = sort_manager.answer_to_wave_length(array, n) 
    # print(response)

#sample_wave_array_data = [1,2,3,4,5]
# convertToWave(sample_wave_array_data, 5)


# Minimum difference pair 
# Basic Accuracy: 70.94% Submissions: 4814 Points: 1
# Given an unsorted array, find the minimum difference between any pair in given array.
 

def largest(array: list[int]):
    array.sort()
    array.reverse()
    print(array[0])

largest([4, 90, 5, 55, 30, 51])