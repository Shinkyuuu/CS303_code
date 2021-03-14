def mod2(num):
    # num is a list of coefficients
    # For every coefficient in num, modulate it by 2
    for i in range(0, len(num)):
        num[i] = num[i] % 2

    return num


def formatNum(num1, num2):
    # Convert num1 and num2 from strings to lists
    numList1 = [num for num in num1]
    numList2 = [num for num in num2]

    # Append zero's to the beginning of the smaller list until they are equal length.
    # This makes it easier to do addition later in the program.
    while len(numList1) != len(numList2):
        if len(numList1) > len(numList2):
            numList2.insert(0, '0')
        else:
            numList1.insert(0, '0')

    return numList1, numList2


def addition(num1, num2):
    numSum = []

    # This for loop performs a XOR operation on the two lists of coefficients.
    # XOR is the equivalent to addition mod 2
    for i in range(0, len(num1)):
        if num1[i] == num2[i]:
            numSum.append(0)
        else:
            numSum.append(1)

    # Reversing the list will makes it easier to convert the coefficients to polynomials.
    numSum.reverse()
    return numSum


def multiplication(num1, num2):
    # Convert the lists to integers
    num1 = int(''.join(str(i) for i in num1))
    num2 = int(''.join(str(i) for i in num2))

    # Do normal multiplication on num1 and num2 and convert the result back into a list of chars.
    solution = [int(i) for i in str(num1 * num2)]

    # Reverse the solution to make polynomial conversion easy.
    solution.reverse()
    return solution


def recursePoly(numList, index=0, before=False, numStr=''):
    # numList = the list of coefficients in reverse order
    # index = the index of the coefficient being converted
    # before = true if there exists a coefficient that has been converted
    #                 before it that's value is '1'. This tells the code whether or not
    #                 to put a '+' after the variable
    # numStr = the polynomial form of numList

    # Return if the end of numList is reached.
    if len(numList) == index:
        return numStr

    # The first variable in the polynomial (If it exists) is '1' and not 'x'.
    # This is a special case.
    if index == 0:

        # If the first variable == 1, append '1' to numStr and turn before to "True".
        if numList[0] == 1:
            before = True
            numStr = '1'

        return recursePoly(numList, index + 1, before, numStr)

    # If the coefficient of the current variable == 1, then insert an 'x^index' to
    # the front of numStr.
    if numList[index] == 1:
        if before:
            numStr = ''.join("x^" + str(index) + '+' + numStr)
        else:
            numStr = ''.join("x^" + str(index))
            before = True

    return recursePoly(numList, index + 1, before, numStr)


def main():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")

    # Convert the nums to lists and make them the same length.
    num1, num2 = formatNum(num1, num2)

    # add/multiply the lists, modulate them by 2, then turn them into polynomial strings.
    numSum = recursePoly(mod2(addition(num1, num2)))
    numMulti = recursePoly(mod2(multiplication(num1, num2)))

    # "x^1" == 'x'
    numSum = numSum.replace("^1", '')
    numMulti = numMulti.replace("^1", '')

    print("Sum:", numSum)
    print("Product:", numMulti)

    return numSum, numMulti


main()
