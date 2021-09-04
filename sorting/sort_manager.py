from timeit import repeat
from random import randint

class SortManager:

    def check_minimum_execution_time_for_algorithm(self, algorithm: str, array: list[int]) -> list[int]:
        # Set up the context and prepare the call to the specified
        # algorithm using the supplied array. Only import the
        # algorithm function if it's not the built-in `sorted()`.
        setup_code = f"from __main__ import {algorithm}" \
            if algorithm != "sorted" else ""

        stmt = f"{algorithm}({array})"

        # Execute the code ten different times and return the time
        # in seconds that each execution took
        times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

        # Finally, display the name of the algorithm and the
        # minimum time it took to run
        print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
        return f"Algorithm: {algorithm}. Minimum execution time: {min(times)}"

    # bubble sort algorithm
    def bubble_sort(self, array: list[int]) -> list[int]: 
        # get the length of the array
        n = len(array)

        # boolean flag for checking values that have been sorted
        already_sorted: bool = True 

        while already_sorted:
            already_sorted = False
            for j in range(n - 1):
                if array[j] > array[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    array[j], array[j + 1] = array[j + 1], array[j]
                    already_sorted = True
        return array


    # insertion sorting
    def insertion_sort(self, array: list[int]) -> list[int]:
    # Loop from the second element of the array until
    # the last element
        for i in range(1, len(array)):
            # This is the element we want to position in its
            # correct place
            key_item = array[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if `key_item` is smaller than its adjacent values.
            while j >= 0 and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1

            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            array[j + 1] = key_item

        return array
        
        # summary of insertion sort
        # We defined for loop for traverse the list from 1 to len(list1).
        # In for loop, assigned a values of list1 in value Every time the loop will iterate the new value will assign to the value variable.
        # Next, we moved the elements of list1[0…i-1], that are greater than the value, to one position ahead of their current position.
        # Now, we used the while to check whether the j is greater or equal than 0, and the value is smaller than the first element of the list.
        # If both conditions are true then move the first element to the 0th index and reduce the value of j and so on.
        # After that, we called the function and passed the list and printed the result.
        # The time complexity of the insertion sort is - O(n2). It uses the two loops for iteration.

    def _split_array(self, array_left: list[int], array_right: list[int]) -> list[int]:
        # The implementation of the merge sort algorithm needs two different pieces:
        #   A function that recursively splits the input in half
        #   A function that merges both halves, producing a sorted array

        # if the first array is empty, then nothing needs to be merge and you can return the second array as the result
        if len(array_left) == 0:
            return array_right

        # if the second array is empty, then nothing needs to be merge and you can return the first array as the result
        if len(array_right) == 0:
            return array_left

        merged_array: list = []
        index_left = index_right = 0

        # now go through both arrays until all the elements are in the result array
        while len(merged_array) < len(array_left) + len(array_right):
            # sort the elements from either array_left or array_right before adding them to merged_array
            if array_left[index_left] <= array_right[index_right]:
                merged_array.append(array_left[index_left])
                index_left += 1
            else:
                merged_array.append(array_right[index_right])
                index_right += 1


            # if you reach the end of either array, then you can add the remaining elements from the other array to the
            #  merged_array and breal the loop
            if index_right == len(array_right):
                merged_array += array_left[index_left:]
                break

            if index_left == len(array_left):
                merged_array += array_right[index_right:]
                break

        return merged_array

        # merge_sort() receives two different sorted arrays that need to be merged together. The process to accomplish this is straightforward:
        # the first 2 conditions check whether either of the arrays is empty. If one of them is, then there’s nothing to merge, so the function returns the other array.
        # a while loop  is started that ends whenever the result contains all the elements from both of the supplied arrays. The goal is to look into both arrays and combine their items to produce a sorted list.
        # after the while line, we compare the elements at the head of both arrays, selects the smaller value, and appends it to the end of the resultant array.
        # we then append any remaining items to the result if all the elements from either of the arrays were already used.

        # With the above function in place, the only missing piece is a function that recursively splits the input array in half and uses merge() to produce the final result:


    def merge_sort(self, array: list[int]) -> list[int]:
        # if the input array contains fewer than two elements, then return it as the result of the function
        if len(array) < 2:
            return array

        midpoint = len(array) // 2
        # sort the array by recursively spliting the input into two equal haves, sorting each half and merging them together into the final result
        return self._split_array(array_left=self.merge_sort(array[:midpoint]), array_right=self.merge_sort(array[midpoint:]))


    def quicksort(self, array: list[int]) -> list[int]:
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
        if len(array) < 2:
            return array

        low, same, high = [], [], []

        # Select your `pivot` element randomly
        pivot = array[randint(0, len(array) - 1)]

        for item in array:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
        return self.quicksort(low) + same + self.quicksort(high)