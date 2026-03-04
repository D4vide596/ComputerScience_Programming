if __name__ == "__main__":
    
    original_words = []

    for i in range(10):
        original_words.append(input("Word = "))
    print("\n\n")
    
    # Alphabetical order
    alphabetical_words = sorted(original_words)
    print("Alphabetical order:")
    for idx, word in enumerate(alphabetical_words):
        if idx != len(alphabetical_words) - 1:
            print(f"'{word}'", end="-")
        else:
            print(f"'{word}'\n\n")
    
    # Reversed alphabetical order
    reverse_alphabetical_words = sorted(original_words, reverse=True)
    print("Reversed alphabetical order:")
    for idx, word in enumerate(reverse_alphabetical_words):
        if idx != len(reverse_alphabetical_words) - 1:
            print(f"'{word}'", end="-")
        else:
            print(f"'{word}'\n\n")

    # Reversed order (modifica in-place)
    original_words.reverse()
    reverse_words = original_words
    print("Reversed order:")
    for idx, word in enumerate(reverse_words):
        if idx != len(reverse_words) - 1:
            print(f"'{word}'", end="-")
        else:
            print(f"'{word}'\n\n")

    # Original order (ora è già modificata)
    print("Original order:")
    for idx, word in enumerate(original_words):
        if idx != len(original_words) - 1:
            print(f"'{word}'", end="-")
        else:
            print(f"'{word}'\n\n")

    # Count
    print("---- Count ----\n")
    count = 0
    for i in range(len(reverse_alphabetical_words)):
        word = reverse_alphabetical_words[i]
        if word == "-":
            continue
        count = 0
        for j in range(len(reverse_alphabetical_words)):
            if word == reverse_alphabetical_words[j]:
                count += 1
                reverse_alphabetical_words[j] = "-"
        print(f"{word}: {count}")
