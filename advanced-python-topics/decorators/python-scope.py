def test_add(n):
    # Here n is scoped variable

    def inner(x, y):
        return x + y + n + m

    return inner


if __name__ == "__main__":
    m = 10
    
    t2 = test_add(2)
    print("t2(5,6) : ", t2(5, 6))

    t3 = test_add(3)
    print("t3(5,6) : ", t3(5, 6))
