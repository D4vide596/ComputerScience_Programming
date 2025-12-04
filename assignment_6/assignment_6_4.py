if __name__ == "__main__":
    
    words = []

    for i in range(10):
        words.append(input(f"Word {i+1} = "))
    
    word_find = input(f"\nInsert the word to find: ")

    if word_find in words:
        idx = words.index(word_find)
        print(f"\nThe word found is the number {idx+1} and is at the index {idx} of the list.")
    else:
        print("The word isn't in the list")