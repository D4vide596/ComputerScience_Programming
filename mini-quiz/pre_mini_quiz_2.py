if __name__ == "__main__":

    #ask the user for their age.
    age = int(input("Enter your age: "))

    if age < 13 : #print child
        print("Child")
    elif 13 <= age < 19: #print teenager
        print("Teenager")
    else: #print adult
        print("Adult")