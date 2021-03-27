import numpy as np


def xor(poly1, poly2, m):
    xoredPoly = []
    #poly1, poly2 = formatPoly(poly1, poly2)

    for i in range(0, len(poly1)):
        if poly1[i] == poly2[i]:
            xoredPoly.append(0)
        else:
            xoredPoly.append(1)

    if (len(xoredPoly) > m):
        xoredPoly.pop(0)
    # Reversing the list will makes it easier to convert the coefficients to polynomials.
    return xoredPoly


def multiBy2(poly, irredPoly, m):
    polyCopy = poly.copy()
    polyCopy.append(0)

    if polyCopy[0] == 1:
        polyCopy = xor(polyCopy, irredPoly, m)
    else:
        polyCopy.pop(0)

    return polyCopy


def bintoNum(binList):
    binStr = ""

    for i in binList:
        binStr += str(i)

    return binStr


def genPrevBin(m):
    prevBin = []
    for i in range(m-1):
        prevBin.append(0)

    prevBin.append(1)
    return prevBin


def genElems(irredPoly, m):
    binLists = {}
    prevBin = genPrevBin(m)
  
    for i in range(0, (2**m)):
        binLists.update({("g^"+str(i)): bintoNum(prevBin)})
        prevBin = multiBy2(prevBin, irredPoly, m)
        
    
    printTable(binLists)
    return 0


def printTable(dictionary):
    for key, value in dictionary.items():
        print("{:<5}  :  {}".format(key, value))


def formatPoly(poly1, poly2):
    coeffs1 = [coeff for coeff in poly1]
    coeffs2 = [coeff for coeff in poly2]

    while len(coeffs1) != len(coeffs2):
        if len(coeffs1) > len(coeffs2):
            coeffs2.insert(0, '0')
        else:
            coeffs1.insert(0, '0')

    return coeffs1, coeffs2


def generatePoly(num):
    factorPoly = [int(coeff) for coeff in str(bin(num)[2:])]
    return np.poly1d(factorPoly)


def testIrr(polynomial, m):
    compositeFlag = False

    for i in range(2, (2**m) + 1):
        factor = generatePoly(i)
        quotient, remainder = np.polydiv(polynomial, factor) 
        remainder = remainder.coefficients % 2
        remainder = [int(elem) for elem in remainder]

        # print("\n     ", polynomial)
        # print("     ---------------")
        # print("     ", factor)
        # print("\n Remainder: ", remainder, "\n")

        if (remainder == [0]):
            #print(" reducible")
            return False

    #print(" irreducible")
    return True


def strToPoly(polynomial):
    poly = [int(coeff) for coeff in polynomial.split(' ')]
    return np.poly1d(poly)


def userInput():
    poly = strToPoly(input(" Polynomial: ").strip())

    #Error Checking
    while (any(poly.coefficients) == 0):
        poly = strToPoly(input(" Try again: ").strip())

    m = int(input(" m: "))

    #Error Checking
    while (m != (len(poly.coefficients)-1)):
        m = int(input(" m must equal the highest degree of the polynomial: "))

    # If polynomial is not irreducible
    if (not testIrr(poly, m)):
        print(" Polynomial is not irreducible")
        return 0

    poly = [int(coeffs) for coeffs in poly]
    genElems(poly, m)
    return 0

userInput()

