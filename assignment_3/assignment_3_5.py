import math

# se voglio solo una funzione
# from math import pi

if __name__ == "__main__":
    r = float(input("Insert circle’s radius: "))
    print(f"Diameter: {2 * r}")
    print(f"Circumference: {2 * math.pi * r}")
    print(f"Area: {math.pi * pow(r,2)}")


