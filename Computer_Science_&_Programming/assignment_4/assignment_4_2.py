if __name__ == "__main__":

    #ask for a number
    num = int(input("Insert a number between <80> and <189>: "))

    #check if the num range and use a match case to fine the range: 
    match num:
        case num if 80 <= num <= 99:
            print(f"The number [{num}] is in the range between <80> and <99>.")
        case num if 100 <= num <= 119:
            print(f"The number [{num}] is in the range between <100> and <119>.")
        case num if 120 <= num <= 139:
            print(f"The number [{num}] is in the range between <120> and <139>.")
        case num if 140 <= num <= 159:
            print(f"The number [{num}] is in the range between <140> and <159>.")
        case num if 160 <= num <= 189:
            print(f"The number [{num}] is in the range between <160> and <189>.")
        case _:
            print(f"The number [{num}] is not in the range between <80> and <189>.")