from random import randint

def create_tri_vector():
    return [randint(-10, 20), randint(-10, 20), randint(-10, 20)]

def sum_vectors(v0, v1):
    return [(v0[0] + v1[0]), (v0[1] + v1[1]), (v0[2] + v1[2])]

def mult_costant(random_value, v):
    return [(v[0] * random_value), (v[1] * random_value), (v[2] * random_value)]

def cross_product(v0, v1):
    return [((v0[1] * v1[2]) - (v0[2] * v1[1])), ((v0[2] * v1[0]) - (v0[0] * v1[2])), ((v0[0] * v1[1]) - (v0[1] * v1[0]))]

if __name__ == '__main__':

    #create two vectors
    v0 = create_tri_vector()
    v1 = create_tri_vector()

    print(f"v0 = ({v0[0]}, {v0[1]}, {v0[2]})")
    print(f"v1 = ({v1[0]}, {v1[1]}, {v1[2]})")

    #sum two vectors
    v2 = sum_vectors(v0, v1)
    print(f"\nv0 + v1 = ({v2[0]}, {v2[1]}, {v2[2]})")

    #multiply a vector with a costant
    rand = randint(-10,10)
    v3 = mult_costant(rand, v0)
    print(f"\n{rand} * v0 = ({v3[0]}, {v3[1]}, {v3[2]})")

    #croos product of 2 vector
    v4 = cross_product(v0, v1)
    print(f"\nv0 * v1 = ({v4[0]}, {v4[1]}, {v4[2]})")


