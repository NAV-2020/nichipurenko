
from random import randint

def bubble_funk(nums):  
    """
    Сортування бульбашкою.
    """
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True


if __name__ == "__main__":

    random_list = [randint(0, 100) for i in range(10)]
    print("Початковий список для сортування:", random_list, '\n')
    bubble_funk(random_list)  
    print("Відсортований список: ", random_list, '\n')