if __name__ == "__main__":

    #ask for variable
    engine_type = int(input("Insert the engine's type: "))
    aircraft_length = int(input("Insert the aircraft's length: "))


    #check condition
    if engine_type == 1 and aircraft_length >= 20: #doesn't specify if it's included
        print("The maximum pressure is 200 bar.")

    elif (engine_type == 2 and 10 < aircraft_length <= 20) or (engine_type == 1 and aircraft_length < 20):
        print("The maximum pressure is 150 bar.")
    
    elif engine_type == 3 or aircraft_length < 10:
        print("The maximum pressure is 100 bar.")
    
    else:
        print("The maximum pressure is 50 bar.")