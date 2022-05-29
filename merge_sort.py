""" 
Implement merge sort in python
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) == 2:
        # just two items
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    # divide
    mid = (len(arr))//2
    # sort each part
    A = merge_sort(arr[:mid])
    B = merge_sort(arr[mid:])
    # merge 
    return merge(A,B)

def merge(A,B):
    """ Compare and merge two already sorted arrays to create one merged and sorted array"""
    la = len(A)
    lb = len(B)

    i,j = 0,0
    merged_arr = []

    while(True):
        if i == la:
            merged_arr.extend(B[j:])
            break
        elif j == lb:
            merged_arr.extend(A[i:])
            break
        elif A[i] == B[j]:
            merged_arr.append(A[i])
            merged_arr.append(B[j])
            i += 1
            j += 1

        elif A[i] < B[j]:
            merged_arr.append(A[i])
            i += 1
        elif A[i] > B[j]:
            merged_arr.append(B[j])
            j += 1

        if i == la and j == lb:
            break

    return merged_arr


def test_merge_sort():
    arr = [5, 4, 3, 2, 1]
    res = merge_sort(arr)
    print(res)
    assert res == [1, 2, 3, 4, 5]

    arr=[10,9,12,8,11]
    res = merge_sort(arr)
    assert res == [8, 9, 10, 11, 12]

    arr=[-10,9,12,8,11]
    res = merge_sort(arr)
    assert res == [-10, 8, 9, 11, 12]

    print("all tests passed")


test_merge_sort()

