if __name__ == "__main__":
    number1 = int(input("Please insert a number: "))
    number2 = int(input("Please insert another number: "))

    print("Is the first number a divisor of the second?", end=" ")
    if number1 % number2 == 0:
        print("True")
    else:
        print("False")