if __name__ == "__main__":

    #ask for grade (0-100)
    grade = int(input("Enter your Grade: "))

    #print letters
    match grade:
        case grade if grade >= 90:
            print("A")
        case grade if grade >= 80:
            print("B")
        case grade if grade >= 70:
            print("C")
        case grade if grade >= 60:
            print("D")
        case grade if grade < 60:
            print("F")