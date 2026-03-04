if __name__ == "__main__":

    #ask for all numbers
    list_numbers = [float(input("Insert 4 non-integer numbers:\n")), float(input()), float(input()), float(input())]
    
    #create variable
    _min = list_numbers[0]
    _max = list_numbers[0]

    #find the lowest and the highest
    for i in range(4):
        
        #check if its smaller then _min
        if list_numbers[i] < _min:
            _min = list_numbers[i]
            continue
        
        #check if its larger than _max
        if list_numbers[i] > _min:
            _max = list_numbers[i]
            continue
    
    print(f"Minimum: {_min}\nMaximum: {_max}")