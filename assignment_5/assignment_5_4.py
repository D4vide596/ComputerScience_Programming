if __name__ == "__main__":

    #ask the numbers
    _min = int(input("Lower bound:"))
    _max = int(input("Upper bound:"))
    print()

    #control if max is greater than min if not correct
    while _max < _min:
        _max = int(input("Upper bound not valid. Retry: "))
        print()

    #some variable + control if we start from a odd or even number
    product = 1
    first_min = _min
    if _min % 2 == 0:
        _min +=1

    #continue untill min is greater than max
    while _min <= _max:

        #multiply it to a variable
        product *= _min

        #add 2 to the variable
        _min += 2

    print(f"Product of all the odd numbers between {first_min} and {_max}: {product}")
    
