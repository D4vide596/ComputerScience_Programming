def merge_file(file_1,file_2,file_name_3,interleaved):
    if interleaved:
        want_interleaved(file_1,file_2,file_name_3)
    else:
        dont_want_interleaved(file_1,file_2,file_name_3)


def want_interleaved(file_1,file_2,file_name_3):
    file1 = open(file_1, "r")
    file2 = open(file_2, "r")

    file3 = open(file_name_3, "w")

    line1 = file1.readline()
    line2 = file2.readline()

    while line1 or line2:
        file3.write(line1)
        file3.write(line2)
        line1 = file1.readline()
        line2 = file2.readline()

    file1.close()
    file2.close()
    file3.close()


def dont_want_interleaved(file_1,file_2,file_name_3):
    file1 = open(file_1, "r")
    file2 = open(file_2, "r")

    file3 = open(file_name_3, "w")
    file3.write(file1.read())
    file3.write(file2.read())

    file1.close()
    file2.close()
    file3.close()


def choose_interleaved():
    choice = input("Do you want to Interleaved the two files? (yes or no) ")
    if choice == "yes":
        return True
    else:
        return False


def choose_new_name_file3():
    return input("Choose a Name for the new File Text: ")


if __name__ == '__main__':

    new_file_name = choose_new_name_file3()
    interleaved = choose_interleaved()
    merge_file("text_file_merge_file1.txt", "text_file_merge_file2.txt", new_file_name, interleaved)