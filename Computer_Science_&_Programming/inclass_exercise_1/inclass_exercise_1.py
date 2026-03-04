if __name__ == "__main__":
    #ask the name of subject
    name_subject = input("What's the name of the Subject: ")

    #ask the numbers of test
    number_of_test = int(input("How many test have you took: "))

    #number of test is greater than 0?
    while (number_of_test <= 0):

        #ask again the numbers of test
        number_of_test = int(input("The test must be greater than 0... How many test have you took: "))

    #set finale_grade = 0
    finale_grade = 0

    #for range the number of test to get all the grades
    for i in range(number_of_test):

        #ask grade of the i+1 test
        grade = float(input(f"What's the grade of the {i+1}° test: "))

        #is the grade of this test between 0 and 6?
        while grade > 6 or grade < 0:

            #ask again the grade of the i+1 test
            grade = float(input(f"The grade must be between 0 and 6... What's the grade of the {i+1}° test: "))

        #sum the grade to the finale_grade variable
        finale_grade += grade

    #divide the sum to the number of test
    finale_grade /= number_of_test

    #see if the grade is equal or greater of and say if I pass
    print(f"You {"passed" if finale_grade >= 4 else "didn't pass"} {name_subject} with a Finale Grade of {finale_grade:.2f}!")