if __name__ == "__main__":
    line = input("Insert the Phrase that you want to control:")
    print(line.strip().replace("*"," ").lower().title().replace("*"," "))