from sort_manager import SortManager

# initialize the sort manager
manager = SortManager()

# sample data
sample_list = [51,7,9,2,6,10]


# using insertion sort
def insertion_sort(array: list[int]) -> list[int]:
    sort_items = manager.insertion_sort(array)
    print(sort_items)


# using bubble sort
def bubble_sort(array: list[int]) -> list[int]:
    sort_items = manager.bubble_sort(array)
    print(sort_items)


# using merge sort
def merge_sort(array: list[int]) -> list[int]:
    sort_items = manager.merge_sort(array)
    print(sort_items)


# using quick sort
def quick_sort(array: list[int]) -> list[int]:
    sort_items = manager.quicksort(array)
    print(sort_items)



bubble_sort(sample_list)
insertion_sort(sample_list)
merge_sort(sample_list)
quick_sort(sample_list)