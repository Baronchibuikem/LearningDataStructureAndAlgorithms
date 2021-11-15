

from typing import Sequence


class SortAnswers:
    def answer_to_wave_length(self, array: list[int], n: int) -> list[int]:
        '''
        array:  array of sorted integers.
        n: number of items in the array.

        output: array of items transformed to a wave array. eg: [1,2,3,4,5] becomes [2,1,3,4,5].
        '''
        # converting a given sorted array to a wave array -> [1,2,3,4,5] becomes [2,1,3,4,5]
        i: int = 1

        while i < n:
            if array[i] > array[i - 1]:
                value = array[i] 
                array[i] = array[i - 1]
                array[i - 1] = value

            i += 2
        return array

    def largest_item_in_array(self, array: list[int]) -> int:
        '''
        array: array of integers.

        output: the largest number in the array
        '''
        array.sort()
        array.reverse()
        largest_number = array[0]
        return largest_number