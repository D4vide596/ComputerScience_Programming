if __name__ == "__main__":

    #let's choose which of the first two triangle we need to create
    first_choice = input("Do you want the A triangle or the the B triangle: ")

    #to decide which of the two to do
    if first_choice == "a" or first_choice == "A":

        #variable for the *
        o = 1

        #loop for creating the lines of the triangle
        for i in range(11):

            for j in range(o):
                print("*", end="")

            
            o += 1

    else: #if b is choosen

        #variable for the *
        o = 11

        #loop for creating the lines of the triangle
        for i in range(11):

            for j in range(o):
                print("*", end="")

            print()
            o -= 1

    #let's choose which of the last two triangle we need to create
    first_choice = input("Do you want the C triangle or the the D triangle: ")

    #to decide which of the two to do
    if first_choice == "c" or first_choice == "C":

        #variable for the spaces
        spaces = 0
        
        #variable for the *
        o = 11

        for i in range(11):
            
            for j in range(spaces):
                print(" ", end="")

            for k in range(o):
                print("*", end="")

            print()

            spaces += 1
            o -= 1

    else: #if d is choosen
        
        #variable for the spaces
        spaces = 11
        
        #variable for the *
        o = 1

        for i in range(11):
            
            for j in range(spaces):
                print(" ", end="")

            for k in range(o):
                print("*", end="")

            print()

            spaces -= 1
            o += 1









#ANOTHER WAY TO DO IT

#CREATE A SQUARE THEN STOP THE J FOR WHEN I EQUALS (A TRIANGLE)
#for i in range (11)
    #for j in range (i)
        #if j<=i
            #print(symbol, end='')
    #print

#CREATE A SQUARE THEN STOP THE J (B TRIANGLE)
#for i in range (11)
    #for j in range (11)
        #if j>=i
            #print(symbol, end='')
    #print