class Person:
    def __init__(self, name, height, weight, gender, bmi=None):
        self.name = name
        self.height = height
        self.weight = weight
        self.gender = gender
        self.bmi = bmi

    def  calculate_bmi(self):
        return round(self.weight/self.height**2, 2)

    def as_dict(self):
        return {"name": self.name,
                "height": self.height,
                "weight": self.weight,
                "gender": self.gender,
                "bmi": self.bmi
                }



class People:
    def __init__(self, list_of_people):
        self.list_of_people = list_of_people

    def calculate_people_bmi(self):
        new_list_of_people = []
        for person in self.list_of_people:
            new_person = Person(person.name, person.height, person.weight, person.gender, person.calculate_bmi())
            new_list_of_people.append(new_person)

        return People(new_list_of_people)

    def calculate_highest_bmi(self):
        person_with_highest_bmi = self.list_of_people[0]
        for person in self.list_of_people:
            if person.bmi > person_with_highest_bmi.bmi:
                person_with_highest_bmi = person
        return person_with_highest_bmi

    def calculate_lowest_bmi(self):
        person_with_lowest_bmi = self.list_of_people[0]
        for person in self.list_of_people:
            if person.bmi < person_with_lowest_bmi.bmi:
                person_with_lowest_bmi = person
        return person_with_lowest_bmi

    def calculate_average_bmi(self):
        sum_bmi = 0
        for person in self.list_of_people:
            sum_bmi += person.bmi
        if len(self.list_of_people) == 0:
            return 0
        return round(sum_bmi/len(self.list_of_people), 2)

    def calculate_male_average_bmi(self):
        sum_bmi = 0
        counter = 0
        for person in self.list_of_people:
            if person.gender == "male":
                sum_bmi += person.bmi
                counter += 1
        if counter == 0:
            return 0
        return round(sum_bmi/counter, 2)

    def calculate_female_average_bmi(self):
        sum_bmi = 0
        counter = 0
        for person in self.list_of_people:
            if person.gender == "female":
                sum_bmi += person.bmi
                counter += 1
        if counter == 0:
            return 0
        return round(sum_bmi/counter, 2)

    def as_dict(self):
        new_list = []
        for person in self.list_of_people:
            new_list.append(person.as_dict())
        return new_list



class FileInterface:

    @staticmethod
    def load_people(file_name):
        with open(file_name, "r") as file:
            list_of_people = []
            for row in file:
                dati = row.strip().split(",")
                person = Person(dati[0].strip(),
                                float(dati[1].strip()),
                                float(dati[2].strip()),
                                dati[3].strip())
                list_of_people.append(person)
        return People(list_of_people)

    @staticmethod
    def save_dict_to_csv(list_of_people, file_name):
        if file_name == "bmi.csv":
            with open(file_name, "w") as file:
                file.write("name, height, weight, gender, bmi\n")
                for person in list_of_people.as_dict():
                    file.write(f"{person['name']}, {person['height']}, {person['weight']}, {person['gender']}, {person['bmi']}\n")
        elif file_name == "highest_bmi.csv":
            with open(file_name, "w") as file:
                file.write("name, height, weight, gender, bmi\n")
                highest_person = list_of_people.calculate_highest_bmi()
                file.write(f"{highest_person.name}, {highest_person.height}, {highest_person.weight}, {highest_person.gender}, {highest_person.bmi}\n")
        elif file_name == "lowest_bmi.csv":
            with open(file_name, "w") as file:
                file.write("name, height, weight, gender, bmi\n")
                lowest_person = list_of_people.calculate_lowest_bmi()
                file.write(f"{lowest_person.name}, {lowest_person.height}, {lowest_person.weight}, {lowest_person.gender}, {lowest_person.bmi}\n")
        elif file_name == "average_bmi.csv":
            with open(file_name, "w") as file:
                file.write("overall, males, females\n")
                average_person_bmi = list_of_people.calculate_average_bmi()
                average_male_person_bmi = list_of_people.calculate_male_average_bmi()
                average_female_person_bmi = list_of_people.calculate_female_average_bmi()
                file.write(f"{average_person_bmi}, {average_male_person_bmi}, {average_female_person_bmi}\n")
        else:
            print(f"wrong file name: {file_name}")


if __name__ == '__main__':

    list_of_people = FileInterface.load_people("people.csv")
    list_of_people_bmi = list_of_people.calculate_people_bmi()
    person_highest_bmi = list_of_people_bmi.calculate_highest_bmi()
    person_lowest_bmi = list_of_people_bmi.calculate_lowest_bmi()
    average_bmi_people = list_of_people_bmi.calculate_average_bmi()
    average_bmi_male =list_of_people_bmi.calculate_male_average_bmi()
    average_bmi_female = list_of_people_bmi.calculate_female_average_bmi()

    FileInterface.save_dict_to_csv(list_of_people_bmi,"bmi.csv")
    FileInterface.save_dict_to_csv(list_of_people_bmi, "highest_bmi.csv")
    FileInterface.save_dict_to_csv(list_of_people_bmi, "lowest_bmi.csv")
    FileInterface.save_dict_to_csv(list_of_people_bmi, "average_bmi.csv")
    FileInterface.save_dict_to_csv(list_of_people_bmi, "try_error.csv")