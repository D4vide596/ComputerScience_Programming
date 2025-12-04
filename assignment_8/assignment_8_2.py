def bmi(weight, height):
    return round(weight / (height**2), 2)

def bmi_each_person(people):
    for person in people:
        bmi_person = bmi(person["weight"], person["height"])
        person["bmi"] = bmi_person
    return people

def highest_bmi (people):
    max_bmi = 0
    people_with_bmi = bmi_each_person((people))
    for person in people_with_bmi:
        if person["bmi"] > max_bmi:
            max_bmi = person["bmi"]
            max_person = person
    return max_person

def lowest_bmi (people):
    low_bmi = 1000
    people_with_bmi = bmi_each_person((people))
    for person in people_with_bmi:
        if person["bmi"] < low_bmi:
            low_bmi = person["bmi"]
            low_person = person
    return low_person

def avarage_bmi (people):
    people_with_bmi = bmi_each_person(people)
    avarage = 0
    for person in people_with_bmi:
        avarage += person["bmi"]
    return round(avarage / len(people_with_bmi), 2)

def avarage_male_bmi (people):
    people_with_bmi = bmi_each_person(people)
    avarage = 0
    count = 0
    for person in people_with_bmi:
        if person["gender"] == "male":
            avarage += person["bmi"]
            count += 1
    return round(avarage / count, 2)

def avarage_female_bmi (people):
    people_with_bmi = bmi_each_person(people)
    avarage = 0
    count = 0
    for person in people_with_bmi:
        if person["gender"] == "female":
            avarage += person["bmi"]
            count += 1
    return round(avarage / count, 2)


if __name__ == '__main__':
    people = [
        {"name": "Sarah Taylor", "height": 1.88, "weight": 52, "gender": "female"},
        {"name": "Daniel Mitchell", "height": 1.53, "weight": 45, "gender": "male"},
        {"name": "Jesse Rodriguez", "height": 1.55, "weight": 57, "gender": "female"},
        {"name": "Lisa Moore", "height": 1.64, "weight": 95, "gender": "female"},
        {"name": "Robert Martinez", "height": 1.64, "weight": 72, "gender": "male"},
        {"name": "Patricia White", "height": 1.79, "weight": 80, "gender": "female"},
        {"name": "Carol Thomas", "height": 1.68, "weight": 96, "gender": "female"},
        {"name": "Andrew Hill", "height": 1.77, "weight": 69, "gender": "male"},
        {"name": "Carol Allen", "height": 1.76, "weight": 85, "gender": "female"},
        {"name": "Edward Mitchell", "height": 1.77, "weight": 59, "gender": "male"},
        {"name": "Andrew Robinson", "height": 1.69, "weight": 102, "gender": "male"},
        {"name": "Edward Robinson", "height": 1.64, "weight": 57, "gender": "male"},
        {"name": "Andrew Nelson", "height": 1.8, "weight": 102, "gender": "male"},
        {"name": "James Robinson", "height": 1.75, "weight": 67, "gender": "male"},
        {"name": "Ashley Nelson", "height": 1.7, "weight": 67, "gender": "female"},
        {"name": "Brian Roberts", "height": 1.82, "weight": 101, "gender": "male"},
        {"name": "Jennifer Wright", "height": 1.62, "weight": 107, "gender": "female"},
        {"name": "George Lee", "height": 1.76, "weight": 79, "gender": "male"},
        {"name": "Donna Perez", "height": 1.79, "weight": 73, "gender": "female"},
        {"name": "Emily Brown", "height": 1.92, "weight": 56, "gender": "female"},
        {"name": "Michael Hernandez", "height": 1.92, "weight": 47, "gender": "male"},
        {"name": "George Martin", "height": 1.78, "weight": 67, "gender": "male"},
        {"name": "Jessica Mitchell", "height": 1.76, "weight": 76, "gender": "female"},
        {"name": "Sarah Lewis", "height": 1.55, "weight": 88, "gender": "female"},
        {"name": "Sandra Clark", "height": 1.51, "weight": 82, "gender": "female"},
        {"name": "Brian Rivera", "height": 1.7, "weight": 66, "gender": "male"},
        {"name": "Sandra Williams", "height": 1.8, "weight": 71, "gender": "female"},
        {"name": "Mary Roberts", "height": 1.91, "weight": 73, "gender": "female"},
        {"name": "Mary Harris", "height": 1.62, "weight": 72, "gender": "female"},
        {"name": "Edward Davis", "height": 1.53, "weight": 89, "gender": "male"},
        {"name": "Jessica Williams", "height": 1.73, "weight": 71, "gender": "female"},
        {"name": "Brian Perez", "height": 1.86, "weight": 70, "gender": "male"},
        {"name": "Matthew Scott", "height": 1.64, "weight": 72, "gender": "male"},
        {"name": "Robert Lopez", "height": 1.66, "weight": 47, "gender": "male"},
        {"name": "John Flores", "height": 1.72, "weight": 60, "gender": "male"},
        {"name": "Patricia Adams", "height": 1.78, "weight": 71, "gender": "female"},
        {"name": "Emily Jones", "height": 1.58, "weight": 85, "gender": "female"},
        {"name": "James King", "height": 1.91, "weight": 59, "gender": "male"},
        {"name": "Margaret Allen", "height": 1.68, "weight": 59, "gender": "female"},
        {"name": "George Nguyen", "height": 1.79, "weight": 91, "gender": "male"},
    ]



    #list of people with bmi
    people_with_bmi = bmi_each_person(people)
    print(f"List of people with BMI:")
    for person in people_with_bmi:
        print(f"name: {person["name"]} height: {person["height"]} weight: {person["weight"]}  gender: {person["gender"]} bmi: {person["bmi"]}")

    #person with highest bmi
    highest_bmi_person = highest_bmi(people)
    print(f"\nPerson with Highest BMI:")
    print(f"name: {highest_bmi_person["name"]} height: {highest_bmi_person["height"]} weight: {highest_bmi_person["weight"]}  gender: {highest_bmi_person["gender"]} bmi: {highest_bmi_person["bmi"]}")

    #person with lowest bmi
    lowest_bmi_person = lowest_bmi(people)
    print(f"\nPerson with Lowest BMI:")
    print(f"name: {lowest_bmi_person["name"]} height: {lowest_bmi_person["height"]} weight: {lowest_bmi_person["weight"]}  gender: {lowest_bmi_person["gender"]} bmi: {lowest_bmi_person["bmi"]}")

    #avarage bmi
    avarage = avarage_bmi(people)
    print(f"\nAverage BMI: {avarage}")

    #avarage male bmi
    avarage_male = avarage_male_bmi(people)
    print(f"Average male BMI: {avarage_male}")

    #avarage female bmi
    avarage_female = avarage_female_bmi(people)
    print(f"Average female BMI: {avarage_female}")