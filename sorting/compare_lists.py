"""
Given two lists of numbers, find the following:
    1- Common items
    2- Only in first list
    3- Only in second list

ex:
    A: [1,2,3,5]
    B: [1,4,5,6,7]

    Common : [1,5]
    Only in A: [2,3]
    Only in B: [4,6,7]
"""

def compare_and_split(A,B):
    common = []
    only_A = []
    only_B = [] 

    la = len(A)
    lb = len(B)
    i,j = 0,0
    while(True):
        if i == la:
            only_B.append(B[j])
            j += 1
        elif j == lb:
            only_A.append(A[i])
            i += 1

        elif A[i] == B[j]:
            common.append(A[i])
            i += 1
            j += 1

        elif A[i] < B[j]:
            only_A.append(A[i])
            i += 1
        elif A[i] > B[j]:
            only_B.append(B[j])
            j += 1

        if i == la and j == lb:
            break

    return common, only_A, only_B



print(compare_and_split([1,2,3,5],[1,4,5,6,7]))