if __name__ == "__main__":

    num = 1
    numbers = []

    while num != 0:

        num = int(input(f"{len(numbers)+1}. number: "))

        if num == 0:
            continue
        else:
            numbers.append(num)

    print("\nInserted 0, finishing number requests.\n")

    # - The mean of all the numbers is
    
    sum_numbers = 0

    for num in numbers:
        sum_numbers += num
    
    mean_numbers = sum_numbers / (len(numbers))

    print(f"- The mean of all the numbers is {mean_numbers:.1f}")


    # - The sum of all the numbers is

    print(f"- The sum of all the numbers is {sum_numbers}")


    #- The inserted negative numbers are: -4,-3

    neg_numbers = []
    pos_numbers = []

    for num in numbers:
        if num < 0:
            neg_numbers.append(num)
        else:
            pos_numbers.append(num)
            
    
    print(f"- The inserted negative numbers are: ", end="")

    for num in neg_numbers:
        if num != neg_numbers[len(neg_numbers)-1]:
            print(num, end=",")
        else:
            print(num)
    
    # - The amount of negative numbers is 2 of 4 => [50%]

    print(f"- The amount of negative numbers is {len(neg_numbers)} of {len(numbers)} => [{(((len(neg_numbers))/(len(numbers)))*100):.0f}%]")
    
    # - The inserted positive numbers are: 1,2

    print(f"- The inserted positive numbers are: ", end="")

    for num in pos_numbers:
        if num != pos_numbers[len(pos_numbers)-1]:
            print(num, end=",")
        else:
            print(num)

    #- The amount of positive numbers is 2 of 4 => [50%]

    print(f"- The amount of positive numbers is {len(pos_numbers)} of {len(numbers)} => [{(((len(pos_numbers))/(len(numbers)))*100):.0f}%]")