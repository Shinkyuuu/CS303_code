import numpy as np


def generatePoly(num):
    factorPoly = [int(coeff) for coeff in str(bin(num)[2:])]
    return np.poly1d(factorPoly)


def testIrr(polynomial, m):
    compositeFlag = False

    for i in range(2, (2**m) + 1):
        factor = generatePoly(i)
        quotient, remainder = np.polydiv(polynomial, factor) 
        remainder = remainder.coefficients % 2

        # print(polynomial)
        # print(factor)
        # print(remainder)
        # print()

        if (remainder.any() == [0.]):
            print("reducible")
            return False

    print("irreducible")
    return True


def format(polynomial):
    poly = [int(coeff) for coeff in polynomial.split(' ')]
    return np.poly1d(poly)


def userInput():
    poly = format(input("Polynomial: ").strip())
    m = int(input("m: "))

    testIrr(poly, m)

userInput()

   # while True:
    #     if (poly.coefficients.all() == 0):
    #         poly = format(input("Try again: ").strip())
    #         break