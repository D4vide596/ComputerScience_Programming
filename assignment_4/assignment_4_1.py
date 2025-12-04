if __name__ == "__main__":

    #ask number 1
    num_1 = int(input("Insert a Number: "))

    #is it positive?
    while num_1 < 0:
        num_1 = int(input("it needs to be a POSITIVE number... insert it again: "))
    
    #ask number 2
    num_2 = int(input("Insert the other Number: "))

    #is it positive?
    while num_2 < 0:
        num_2 = int(input("it needs to be a POSITIVE number... insert it again: "))
    
    #is the remainder 0?
    if num_1 % num_2 == 0:

        #say to the user what's the result of the division
        print(f"The result of the division is {num_1/num_2}")
    else:

        #say the two numbers are not multiple
        print("The two numbers are not Multiple")
    
