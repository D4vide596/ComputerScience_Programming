def is_it_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    number = int(input("Enter a Number to see if it's Prime: "))
    if is_it_prime(number):
        print("The Number is Prime")
    else:
        print("The Number is not Prime")

    print("Numbers from 1 to 100:")
    for i in range(2,100):
        if is_it_prime(i):
            print(f"{i} ", end="")