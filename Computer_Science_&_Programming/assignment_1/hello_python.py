# Using the code examples in problem set 1,
# try to write a program that can calculate 
# the final grade for this course as a weighted 
# average of mini-quizzes, in-class assignments, and tests

if __name__ == '__main__':
    # request user input

 test1_T = (float(input("Insert your Grade for the Test 1 of the Theory Module:")))* 0.3

 test2_T = (float(input("Insert your Grade for the Test 2 of the Theory Module:")))* 0.5

 Mini_quizzes1_T = (float(input("Insert your Grade for the Mini-quizzes 1 of the Theory Module:")))* 0.1
 
 Mini_quizzes2_T = (float(input("Insert your Grade for the Mini-quizzes 2 of the Theory Module:")))* 0.1

 test1_L = (float(input("Insert your Grade for the Test 1 of the Lab Module:")))* 0.3

 test2_L = (float(input("Insert your Grade for the Test 2 of the Lab Module:")))* 0.5

 In_Class_Assignments1_L = (float(input("Insert your Grade for the In-class Assignments 1 of the Lab Module:")))* 0.1

 In_Class_Assignments2_L = (float(input("Insert your Grade for the In-class Assignments 2 of the Lab Module:")))* 0.1

 FinaleGradeT = (test1_T + test2_T + Mini_quizzes1_T + Mini_quizzes2_T)
 FinaleGradeL = (test1_L + test2_L + In_Class_Assignments1_L + In_Class_Assignments2_L)

 print("The Finale Grade for the Thoery Module it's: " + str(FinaleGradeT))
 print("The Finale Grade for the Lab Module it's: " + str(FinaleGradeL))

#
#name = input("What is your name?: ")
#    print("Hi " + name + " welcome to the course")
#    num1 = input("Insert an integer number: ")
#    num2 = input("Insert another integer number: ")
#    num1 = int(num1)
#    num2 = int(num2)
#    # do calculations
#    num_sum = num1 + num2
#    num_diff = num1- num2
#    num_multi = num1 * num2
#    # print results
#    print(str(num1) + " + " + str(num2) + " = " + str(num_sum))
#    print(str(num1) + "- " + str(num2) + " = " + str(num_diff))
#    print(str(num1) + " * " + str(num2) + " = " + str(num_multi))
    