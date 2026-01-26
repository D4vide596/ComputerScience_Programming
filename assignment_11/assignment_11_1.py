class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = float(numerator)
        self.denominator = float(denominator)

    def  __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def opposite(self):
        return Fraction(-self.numerator,self.denominator)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)

    def prettify(self):
        def get_gcd(a,b):
            if b == 0:
                return a
            r = a % b
            if r == 0:
                return b
            return get_gcd(b, r)

        common = get_gcd(abs(self.numerator), abs(self.denominator))

        self.numerator = self.numerator / common
        self.denominator = self.denominator / common

        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return self.prettify()


if __name__ == '__main__':

    f1 = Fraction(float(input("Insert a Numerator: ")), float(input("Insert a Denominator: ")))
    f2 = Fraction(float(input("Insert a Numerator: ")), float(input("Insert a Denominator: ")))


    print(f"opposite of f1 = {f1.opposite()}")
    print(f"inverse of f1 = {f1.inverse()}")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 * f2 = {f1 * f2}")