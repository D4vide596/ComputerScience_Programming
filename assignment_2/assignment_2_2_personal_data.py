if __name__ == '__main__':
    first_name = input("Insert your first name: ")
    last_name = input("Insert your last name: ")
    address = input("Insert your address: ")
    year_of_birth = int(input("Insert your year of birth: "))

    age = 2025 - year_of_birth

    print(f"\n---------------------------------\n\n" 
          f"First Name: {first_name}\n" \
          f"Last Name : {last_name}\n" \
          f"Address: {address}\n" \
          f"Year of birth: {year_of_birth}\n" \
          f"Age: {age}")