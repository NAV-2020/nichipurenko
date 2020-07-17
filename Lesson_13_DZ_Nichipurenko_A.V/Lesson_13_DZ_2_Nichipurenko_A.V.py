
from random import randint

def partition(nums, low, high):  
    """
    Швидке сортування.
    """
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_fun(nums):  
    def quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            quick_sort(items, low, split_index)
            quick_sort(items, split_index + 1, high)

    quick_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":

    random_list = [randint(0, 100) for i in range(10)]
    print("Початковий список для сортування:", random_list, '\n')
    quick_fun(random_list)  
    print("Відсортований список: ", random_list, '\n')
