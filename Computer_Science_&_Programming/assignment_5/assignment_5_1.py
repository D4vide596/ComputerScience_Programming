if __name__ == "__main__":

    #ask the how many number we need to find
    limits = int(input("Enter the number of Armstrong numbers to search for: "))
    found_all = False

    #create variable
    number = 0
    sum_of_parts = 0
    armstrong_number_found = 0

    #loop for stop us when we finished the numbers
    while(not found_all):

        #lenght of the number
        number_lenght = len(str(number))

        #sum at a variable the power of each number
        for j in range(int(number_lenght)):
            sum_of_parts += int(str(number)[j]) ** number_lenght
        
        #say if they are the same
        if sum_of_parts == number:
            print(f"Armstrong number found ({armstrong_number_found + 1}): --> {number}")
            armstrong_number_found += 1
            if armstrong_number_found == limits:
                found_all = True

        #update the variable
        number += 1
        sum_of_parts = 0

    print(f"Found {limits} Armstrong numbers in the first {number} numbers checked")
