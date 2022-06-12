""" 
Implement bubble sort in python
"""

def bubble_sort(arr):
    print("="*20)
    print(f"Input : {arr}")

    l = len(arr)
    while(True):
        swapped = False

        for i in range(l-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        print(f"Iteration done: {arr}")
        # if no swapping happened in this pass, then the array is already sorted
        # so break the loop
        if not swapped:
            break




def test_bubble_sort():
    arr = [5, 4, 3, 2, 1]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr=[10,9,12,8,11]
    bubble_sort(arr)
    assert arr == [8, 9, 10, 11, 12]

    arr=[-10,9,12,8,11]
    bubble_sort(arr)
    assert arr == [-10, 8, 9, 11, 12]

    print("all tests passed")


test_bubble_sort()

