def surface_of_cuboid(w, h, d):
    return 2 * ((w * h) + (w * d) + (h * d))

def volume_of_cuboid(w,h,d):
    return w * h * d

def error(a):
    while a <= 0:
        a = int(input("Needs to be Greater than 0. try again: "))
    return a


if __name__ == '__main__':

    list_volume = []
    list_area = []

    print("Enter the First cuboids:")
    w1 = int(input("Width: "))
    while w1 <= 0:
        w1 = error(w1)

    h1 = int(input("Height: "))
    while h1 <= 0:
        h1 = error(h1)

    d1 = int(input("Depth: "))
    while d1 <= 0:
        d1 = error(d1)

    list_volume.append(volume_of_cuboid(w1,h1,d1))
    list_area.append(surface_of_cuboid(w1,h1,d1))

    print("\nEnter the Second cuboids:")
    w2 = int(input("Width: "))
    while w2 <= 0:
        w2 = error(w2)

    h2 = int(input("Height: "))
    while h2 <= 0:
        h2 = error(h2)

    d2 = int(input("Depth: "))
    while d2 <= 0:
        d2 = error(d2)

    list_volume.append(volume_of_cuboid(w2, h2, d2))
    list_area.append(surface_of_cuboid(w2, h2, d2))

    print("\nEnter the Third cuboids:")
    w3 = int(input("Width: "))
    while w3 <= 0:
        w3 = error(w3)

    h3 = int(input("Height: "))
    while h3 <= 0:
        h3 = error(h3)

    d3 = int(input("Depth: "))
    while d3 <= 0:
        d3 = error(d3)

    list_volume.append(volume_of_cuboid(w3, h3, d3))
    list_area.append(surface_of_cuboid(w3, h3, d3))

    total_volume = sum(list_volume)
    total_surface = sum(list_area)

    print(f"\nTotal Volume is {total_volume}")
    print(f"Total Surface is {total_surface}")