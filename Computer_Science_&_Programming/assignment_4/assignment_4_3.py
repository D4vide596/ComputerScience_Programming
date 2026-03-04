from math import radians, sqrt, cos

if __name__ == "__main__":
    
    #ask the sides and the angle
    side_a = int(input("Insert the length of the side A: "))
    side_b = int(input("Insert the length of the side B: "))
    angle_alfa = radians(float(input("Insert the angle alfa in degrees: ")))

    #find the other side using the formula
    side_c = sqrt(side_a**2 + side_b**2 - (2 * side_a * side_b * cos(angle_alfa)))

    #say the answer
    print(f"The length of the side C is {side_c}")