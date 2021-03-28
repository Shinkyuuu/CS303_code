
# Checking polynomial irreducibility would be simpler with
# numpy's poly1d class but I didn't know if I was allowed to use that
# so I didn't.


# Print dictionary in the form of a table.
def printTable(dictionary):
    for key, value in dictionary.items():
        print("{:<5}  :  {}".format(key, value))


# XOR two polynomials together.
def xor(poly1, poly2, m = 999):
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


# Generate the binary representation of one that's number of leading zeros match 
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


# Generate binary number in list form.
def genBinList(decNum):
    return  [int(coeff) for coeff in str(bin(decNum)[2:])]
    

# Add a specified amount of zeros to the end of a list.
def appendZeros(poly, amount):
    for i in range(amount):
        poly.append(0)

    return poly


# Remove leading zeros from a binary number in list form.
def removeZeros(poly):
    # While the list contains at least one elements, remove leading zeros.
    while (len(poly) > 1) and (poly[0] == 0):
        poly.pop(0)

    return poly


# Check if the user inputted polynomial is irreducible
def irredCheck(poly, m):
    # Divide it by every possible factor within the same field.
    for i in range(2, (2 ** m) + 1):
        if not hasRemainder(poly, genBinList(i)):
            return False

    return True
        

# Check if the user inputted polynomial divided by a 
# polynomial of a lesser degree has a remainder.
def hasRemainder(poly1, poly2):
    # irredPoly = denominator
    irredPoly = poly1.copy()

    while True:
        # binPoly = numerator
        # diff = difference in length
        binPoly = poly2.copy()
        diff = abs(len(irredPoly)-len(binPoly))

        # Make both polynomials the same length.
        # This is the same as multiplying the lesser polynomial by a 
        # power of 'g' to make their degrees the same.
        if len(irredPoly) > len(binPoly):
            binPoly = appendZeros(binPoly, diff)
        # If binPoly is greater than irredPoly, there is a remainder.
        elif len(irredPoly) < len(binPoly):
            return True
        # If both polynomials are equal, the remainder is zero.
        elif irredPoly == binPoly:  
            return False
        # If their lengths are the same, check if binPoly is greather 
        # than irredPoly.
        else:
            for i in range(len(irredPoly)-1, 0):         
                if irredPoly[i] < binPoly[i]:
                    return True

        # xor them together and remove the leading zeros.
        irredPoly = xor(irredPoly, binPoly)
        irredPoly = removeZeros(irredPoly)


# Convert binary from string form to list form.
def strToList(polynomial):
    return [int(coeff) for coeff in polynomial.split(' ')]


# Recieve and verify user inputs.
def userInput():
    # poly = alleged irreducible polynomial.
    poly = strToList(input(" Polynomial: ").strip())

    # Error Checking
    while (any(poly) == 0):
        poly = strToList(input(" Try again: ").strip())

    # m = degree of irreducible polynomial
    m = int(input(" m: "))

    # Error Checking
    while (m != (len(poly) - 1)):
        m = int(input(" m must equal the highest degree of the polynomial: "))

    # If polynomial is not irreducible
    if (not irredCheck(poly, m)):
        print(" Polynomial is reducible")
        return 0
    
    # Return the nonxero elems of GF(2^m)
    return genElems(poly, m)


userInput()


