from dp_fibo import fib 
from trig_functions import sin, cos


if __name__ == "__main__":
    print("testing all math")
    choice = input("Choose a function: sin, cos, fib: ")
    if choice == "sin":
        x = float(input("Enter radian value: "))
        print(f"Sin: {sin(x)}")
    elif choice == "cos":
        x = float(input("Enter radian value: "))
        print(f"Cos: {cos(x)}")
    elif choice == "fib":
        n = int(input("Enter a number: "))
        print(f"Fib: {fib(n)}")
    else:
        print("Invalid choice")
