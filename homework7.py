import numpy as np

# Print dictionary in the form of a table.
def printTable(dictionary):
    for key, value in dictionary.items():
        print("{:<5}  :  {}".format(key, value))


# XOR two polynomials together.
def xor(poly1, poly2, m):
    # xoredPoly = the solution polynomial.
    xoredPoly = []

    # XOR every element in each polynomial.
    for i in range(0, len(poly1)):
        if poly1[i] == poly2[i]:
            xoredPoly.append(0)
        else:
            xoredPoly.append(1)

    # If the amount of leading zeros makes the polynomial fall 
    # out of the field, remove them.
    if (len(xoredPoly) > m):
        xoredPoly.pop(0)

    return xoredPoly


# Multiply polynomial in binary form by 2.
def multiBy2(poly, irredPoly, m):
    polyCopy = poly.copy()
    polyCopy.append(0)

    # If polynomial falls out of the field, XOR it by the irreducible polynomial.
    if polyCopy[0] == 1:
        polyCopy = xor(polyCopy, irredPoly, m)
    else:
        polyCopy.pop(0)

    return polyCopy


# Convert binary number from list to string.
def binToStr(binList):
    binStr = ""

    for i in binList:
        binStr += str(i)

    return binStr


# Generate the binary representation of '1' that's number of leading zeros match 
# the degree of the irreducible polynomial.
def genPrevBin(m):
    prevBin = []

    for i in range(m - 1):
        prevBin.append(0)

    prevBin.append(1)
    return prevBin


# Generate the nonzero elements of GF(2^m) with their associated power of g.
def genElems(irredPoly, m):
    # binDict = dictionary of powers of g and their binary representations (e.g. {"g^0" : "0001"} ).
    # prevBin = the previous binary representation that'll be multiplied by 2 to get the current one.
    binDict = {}
    prevBin = genPrevBin(m)

    # For every element in GF(2^m), multiply the previous binary number starting from 1 by 2 and mod by 
    # irreducible polynomial if needed.
    for i in range(0, (2 ** m)):
        binDict.update({("g^" + str(i)): binToStr(prevBin)})
        prevBin = multiBy2(prevBin, irredPoly, m)

    printTable(binDict)

    return binDict


# Generates binary number in GF(2^m) in polynomial form
def genBinPoly(decNum):
    # factorPoly is initialized as a list form of a binary number.
    # It is then converted to numpy polynomail.
    factorPoly = [int(coeff) for coeff in str(bin(decNum)[2:])]
    return np.poly1d(factorPoly)


# Determine whether the user inputted polynomial is irreducible.
def testReducibility(polynomial, m):
    compositeFlag = False

    # Divide the polynomial by every element in GF(2^m)
    # If any of their remainders is '0', then the polynomial is reducible 
    for i in range(2, (2 ** m) + 1):
        # factor = a polynomial in GF(2^m)
        factor = genBinPoly(i)
        quotient, remainder = np.polydiv(polynomial, factor)

        #Uncomment to see what is being divided by what and what the remainders are
        # print("\nDivision: ")
        # print(polynomial)
        # print("_______________")
        # print(factor)
        # print("\nRemainder: ")
        # print(remainder, "\n")

        # Mod the remainder by 2 and turn it into a list of integers
        remainder = remainder.coefficients % 2
        remainder = [int(elem) for elem in remainder]

        if (remainder == [0]):
            # print(" reducible")
            return False

    # print(" irreducible")
    return True


# Convert user input polynomial string to numpy polynomial.
def strToPoly(polynomial):
    poly = [int(coeff) for coeff in polynomial.split(' ')]
    return np.poly1d(poly)


# Recieve and verify user inputs.
def userInput():
    # poly = alleged irreducible polynomial.
    poly = strToPoly(input(" Polynomial: ").strip())

    # Error Checking
    while (any(poly.coefficients) == 0):
        poly = strToPoly(input(" Try again: ").strip())

    # m = degree of irreducible polynomial
    m = int(input(" m: "))

    # Error Checking
    while (m != (len(poly.coefficients) - 1)):
        m = int(input(" m must equal the highest degree of the polynomial: "))

    # If polynomial is not irreducible
    if (not testReducibility(poly, m)):
        print(" Polynomial is not irreducible")
        return 0

    # Turn poly into a list of integer coefficients
    poly = [int(coeffs) for coeffs in poly]
    
    # Return the nonxero elems of GF(2^m)
    return genElems(poly, m)


userInput()

