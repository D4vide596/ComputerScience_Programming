import math


def my_sin(x, num_terms):
    value = 1
    number = 3
    result = x

    for i in range(1, num_terms):
        for n in range(1, number + 1):
            value *= x / n

        if i % 2 == 0:
            result += value
        else:
            result -= value

        number += 2
        value = 1

    return result

def my_cos(x, num_terms):
    value = 1
    number = 2
    result = 1

    for i in range(1, num_terms):
        for n in range(1, number + 1):
            value *= x / n

        if i % 2 == 0:
            result += value
        else:
            result -= value

        number += 2
        value = 1

    return result

if __name__ == '__main__':
    num_terms = 9

    print(f"x = 0")
    print(f"\tmy_sin = {my_sin(0,num_terms)}")
    print(f"\tsin = {math.sin(0)}")
    print(f"\n\tmy_cos = {my_cos(0,num_terms)}")
    print(f"\tcos = {math.cos(0)}")

    print(f"\nx = π/6")
    print(f"\tmy_sin = {my_sin(math.pi/6, num_terms)}")
    print(f"\tsin = {math.sin(math.pi/6)}")
    print(f"\n\tmy_cos = {my_cos(math.pi/6, num_terms)}")
    print(f"\tcos = {math.cos(math.pi/6)}")

    print(f"\nx = π/4")
    print(f"\tmy_sin = {my_sin(math.pi / 4, num_terms)}")
    print(f"\tsin = {math.sin(math.pi / 4)}")
    print(f"\n\tmy_cos = {my_cos(math.pi / 4, num_terms)}")
    print(f"\tcos = {math.cos(math.pi / 4)}")

    print(f"\nx = π/3")
    print(f"\tmy_sin = {my_sin(math.pi / 3, num_terms)}")
    print(f"\tsin = {math.sin(math.pi / 3)}")
    print(f"\n\tmy_cos = {my_cos(math.pi / 3, num_terms)}")
    print(f"\tcos = {math.cos(math.pi / 3)}")

    print(f"\nx = π/2")
    print(f"\tmy_sin = {my_sin(math.pi / 2, num_terms)}")
    print(f"\tsin = {math.sin(math.pi / 2)}")
    print(f"\n\tmy_cos = {my_cos(math.pi / 2, num_terms)}")
    print(f"\tcos = {math.cos(math.pi / 2)}")