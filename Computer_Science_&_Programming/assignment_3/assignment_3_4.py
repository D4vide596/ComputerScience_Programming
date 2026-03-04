if __name__ == "__main__":
    val_1 = input("Insert first value: ")
    val_2 = input("Insert second value: ")

    print("Values before swapping:")
    print(f"\tfirst_val: {val_1}")
    print(f"\tsecond_val: {val_2}")
    print("Values after swap:")

    temp_val = val_1
    val_1 = val_2
    val_2 = temp_val

    print(f"\tfirst_val: {val_1}")
    print(f"\tsecond_val: {val_2}")

    