#file Rational.py
class Rational:
    def __init__(self, n, d):

        if (not isinstance (n, int) or not isinstance (d, int)):
            raise TypeError ("The numerator and denominator must both be of type int!")
        if d == 0:
            raise ZeroDivisionError ("Denominator cannot be zero!")
        elif n == 0:
            d = 1
        # now go thorugh Euclid's GCD algorithm to reduce to lowest terms
        a = n
        b = d

        remainder = a % b
        while remainder != 0:
            a = b
            b = remainder
            remainder = a % b
        # b is now the GCD (n, d)
        self.__numerator = n // b
        self.__denominator = d // b

        #__add__(self,1)

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def __add__ (self, addend):
        top = self.getNumerator() * addend.getDenominator() + self.getDenominator()*addend.getNumerator()
        bottom = self.getDenominator() * addend.getDenominator()
        return Rational (top, bottom)

    def __sub__(self, subtrahend):
        top = self.getNumerator() * subtrahend.getDenominator() - self.getDenominator()*subtrahend.getNumerator()
        bottom = self.getDenominator() * subtrahend.getDenominator()
        return Rational (top, bottom)

    def __mul__(self, multiplier):
        top = self.getNumerator() * multiplier.getNumerator()
        bottom = self.getDenominator() * multiplier.getDenominator()
        return Rational (top, bottom)

    def __floordiv__ (self, dividend):
        return self * Rational (dividend.getDenominator(), dividend.getNumerator())
    
    def __str__(self):
        return str(self.__numerator) + " / " + str(self.__denominator)


    #float will divide numerator by denominator
    def __float__ (self):
        return  self.getNumerator() / self.getDenominator()


#create object i am a float
i_am_a_float = Rational(2,4)
#print the call of float on i am a float
print(i_am_a_float.__float__())









