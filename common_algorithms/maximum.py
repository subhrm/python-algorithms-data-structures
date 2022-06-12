def maximum(arr, n):
    arr.sort()
    return arr[-n:]


if __name__ == "__main__":
    arr = [12,6, 8, 9, 10, 1, 2, 3, 4, 5, 7]
    n = int(input("Enter a number: "))
    print(maximum(arr, n))
    