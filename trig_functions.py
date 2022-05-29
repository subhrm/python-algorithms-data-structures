import math

def sin(x):
    return (math.sin(x))

def cos(x):
    return (math.cos(x))

if __name__ == "__main__":
    print("Testing Trig Functions")
    x = float(input("Enter radian value: "))
    print(f"Sin: {sin(x)} cos: {cos(x)}")

if __name__ == "trig_functions":
    print("Thanks for importing trig_functions. Good luck!")