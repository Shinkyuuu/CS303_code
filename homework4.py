# Cody Park / CS 303


#  Accepts 2 bytes in list form and XORs them
def xor(num1, num2):
    xorNum = []

    for i in range(0, len(num1)):
        xorNum.append((num1[i] + num2[i]) % 2)

    if len(xorNum) > 8:
        xorNum.pop(0)

    return xorNum


# Accepts a byte in the form of a list and returns it multiplied by 2 in the same form.
def multiBy2(binList):
    # irrNum = irreducible polynomial given in class.
    # binListCopy = copy of binList.
    irrNum = [1, 0, 0, 0, 1, 1, 0, 1, 1]
    binListCopy = binList.copy()

    binListCopy.append(0)

    # If byte shifted left falls out of the field, XOR it to irrNum.
    if binListCopy[0] == 1:
        binListCopy = xor(binListCopy, irrNum)
    else:
        binListCopy.pop(0)

    return binListCopy


# Accepts a byte in the form of a list and returns it multiplied by 3 in the same form.
def multiBy3(binList):
    # binList2 = binList multiplied by 2.
    binList2 = multiBy2(binList)

    return xor(binList, binList2)


# Converts hex digit to a byte in list form.
def hexToByte(hexList):
    # Turn hex to byte in integer form.
    # I don't do any math when converting binary to hex and vice versa
    # so I didn't make my own conversion function.
    byte = "{0:08b}".format(int(hexList, 16))

    # Turn integer to list
    return [int(x) for x in str(byte)]


# Converts hex digit matrix to byte matrix.
def hexToByteMtx(hexMtx):
    # Individually convert every hex digit in matrix to byte.
    for hexRow in hexMtx:
        for i in range(len(hexRow)):
            hexRow[i] = hexToByte(hexRow[i])

    return hexMtx


# Converts byte matrix to hex digit matrix.
def byteToHexMtx(mtx):
    # Individually convert every byte in matrix to hex digit.
    for row in mtx:
        for i in range(len(row)):
            string = hex(int("".join([str(bit) for bit in row[i]]), 2))

            # Remove unwanted letters and make it look like it does in the book (e.g. 0x5 -> 05).
            row[i] = string.replace("x", "")

            if len(string) > 3:
                row[i] = row[i][1:]

    return mtx


# Accepts the column mixing matrix and the matrix to be mixed and mixes it.
def mixCol(mixedColMtx, userMtx):
    # SolutionMtx = unfilled solution matrix.
    # rowNum iterates from 0-3 over the course of 16 loops.
    solutionMtx = [[], [], [], []]
    rowNum = 0

    for i in range(0, 16):
        # tempList = XORed bytes that will eventually become a mixed byte within solutionMtx.
        # colNum iterates from 0-3 four times over the course of 16 loops.
        tempList = [0, 0, 0, 0, 0, 0, 0, 0]
        colNum = i % 4

        if (i % 4) == 0 and i != 0:
            rowNum += 1

        # Multiply the elements of a mixedColMtx row by a userMtx column.
        # Do this for every row and column.
        for colRow in range(0, 4):
            givenHex = mixedColMtx[rowNum][colRow]
            currentBin = userMtx[colRow][colNum]

            if givenHex == 2:
                copyUserMtx = (multiBy2(currentBin))
            elif givenHex == 3:
                copyUserMtx = (multiBy3(currentBin))
            else:
                copyUserMtx = (userMtx[colRow][colNum])

            # Add the results of the row and column products together.
            tempList = xor(tempList, copyUserMtx)
        solutionMtx[rowNum].append(tempList)
        # Convert byte matrix to hex digit matrix
    byteToHexMtx(solutionMtx)

    return solutionMtx


# Ask user whether to answer question 5e or custom matrix, then convert it to a usable (byte list) format.
def askUser():
    # mixedColMtx = the matrix to multiply to the inputted matrix to perform mixColumn operation.
    # testMtx = book example of matrix so I know if the code works.
    # homeworkMtx = question 5e matrix.
    mixedColMtx = [[2, 3, 1, 1],
                                [1, 2, 3, 1],
                                [1, 1, 2, 3],
                                [3, 1, 1, 2]]
    testMtx = [["ab", "8b", "89", "35"],
                       ["40", "7f", "f1", "05"],
                       ["f0", "fc", "18", "3f"],
                       ["c4", "e4", "4e", "2f"]]
    homeworkMtx = [["7c", "6b", "01", "d7"],
                                  ["f2", "30", "fe", "63"],
                                  ["2b", "76", "7b", "c5"],
                                  ["ab", "77", "6f", "67"]]

    # Ask user whether to mix homeworkMtx or custom matrix.
    answer = input("Would you like to answer question 5e (1) or enter custom hex matrix (anything else): ")

    if answer == '1':
        # To test testMtx, set userMtx equal to it.
        userMtx = homeworkMtx
    else:
        rowMtx = []
        userMtx = []
        # Sample input: 7c 6b 01 d7 f2 30 fe 63 2b 76 7b c5 ab 77 6f 67
        rawUserMtx = input("Input full matrix row by row (e.g. 07 2a fb 3a 2b...): ").split(" ")

        for i in range(1, 17):
            rowMtx.append(rawUserMtx[i - 1])

            if (i % 4) == 0:
                userMtx.append(rowMtx.copy())
                rowMtx.clear()

    # Turn hex matrix to byte matrix.
    hexToByteMtx(userMtx)

    # Do the actual mixing
    return mixCol(mixedColMtx, userMtx)


# Main func.
def main():
    solutionMtx = askUser()

    print("\n The mixed matrix is now... ")
    for element in solutionMtx:
        print(element)

    return solutionMtx


main()
