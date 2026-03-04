#FATTO DAL PROF


if __name__ == "__main__":

    #ask for 6 number
    num_list = []

    input_message = "Insert a number: "

    while len(num_list) < 6:
        num = int(input(input_message))
        if num < 6 or num > 666:
            print(f"Invalid number [{num}]. It is out of range!", end=" ")
            input_message = "Insert another number: "
            #CONTINUE TORNA INDIETRO E RICONTROLLA DAL WHILE
            continue
            
        if num in num_list:
            print(f"Invalid number [{num}]. It was already inserted!", end=" ")
            input_message = "Insert another number: "
            continue

        num_list.append(num)
        input_message = "Insert a number: "
    
    num_list.sort()
    print("\nNumber =>", end=" ")
    for idx, el in enumerate(num_list):
        if idx != len(num_list) - 1:
            print(el, end=", ")
        else:
            print(el)