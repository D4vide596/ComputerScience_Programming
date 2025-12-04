if __name__ == "__main__":
    vector = [int(input("Insert the x coordinate of the vector: ")),
               int(input("Insert the y coordinate of the vector: ")),
               int(input("Insert the z coordinate of the vector: "))]
    value = int(input("Insert the value to multiplicate the vector: "))

    print("Initial vector:")
    print(f"\tx,y,z => {vector[0]},{vector[1]},{vector[2]}\n")
    print(f"Value of multiplication: {value}\n")
    print(f"Resulting vector:")
    print(f"\tx,y,z => {vector[0]*value},{vector[1]*value},{vector[2]*value}")