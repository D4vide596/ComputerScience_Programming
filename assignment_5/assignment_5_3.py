if __name__ == "__main__":

    #print start
    print("Iteration # Value of Pi\n---------------------------")

    #variable
    rank = 0
    value = 4.0
    divisor = 3

    #loop
    for i in range(10000):
        
        #print the result
        print(f"{rank}\t{value}")
        rank += 1
        
        #if i is even subract the division if odd sum it
        if i % 2 == 0:
            value -= (4/divisor)
            #keep increasing the divisor
            divisor += 2
        else:
            value += (4/divisor)
            #keep increasing the divisor
            divisor += 2