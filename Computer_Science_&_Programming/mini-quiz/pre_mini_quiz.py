if __name__ == "__main__":

    #ask for 5 numbers #save numbers in a list
    list_number = []
    even_number = 0 #variable for counting even
    odd_number = 0 #variable for counting odd
    
    #5 elementi
    for i in range(5):

        #append for adding a number in the list... no int control..
        list_number.append(int(input(f"Enter Number {i+1}: ")))
        
        #how many are even and odd
        if list_number[i] % 2 == 0:
            even_number += 1
        else:
            odd_number += 1

    #say the list, numbers of even, number of odd
    print(f"Numbers: {list_number}")
    print(f"Even numbers: {even_number}")
    print(f"Odd numbers: {odd_number}")