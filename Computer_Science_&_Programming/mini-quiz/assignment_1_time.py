if __name__ == "__main__":
    # Ask the user for an amount of time in seconds
    # Example: Enter an amount of seconds: 12735
    seconds = int(input("Enter an amount of seconds: "))

    # Ask the user for an amount of time in minutes
    # Example: Enter an amount of minutes: 75
    minutes = int(input("Enter an amount of minutes: "))

    # Print what the program will calculate
    print(f"{seconds} seconds + {minutes} minutes is equal to:")

    # Convert seconds into minutes and seconds
    minutes_to_add = seconds // 60       # total full minutes in 'seconds'
    remaining_seconds = seconds % 60     # leftover seconds

    # Add the converted minutes to the total minutes
    total_minutes = minutes + minutes_to_add

    # Convert total minutes into hours and minutes
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    # Print the final result
    print(f"'{hours}' hours, '{remaining_minutes}' minutes, and '{remaining_seconds}' seconds")
