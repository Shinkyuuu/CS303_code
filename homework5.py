# Recursively add pseudorandom integer values to a list until the period is complete
def recurseBBS(n, s, xList=[],  initX=0, prevX=-1, counter=0):
    # xList = list in which the prandom integers will be added to.
    # initX = initial X value.
    # counter = added to by 1 every iteration, inevitably becomes the period.
    # prevX = last iteration's X value.

    # If on the first iteration, set initial values. Else, perform BBS algorithm.
    if prevX == -1:
        # currX = current prandom X value.
        currX = (s ** 2) % n
        initX = currX
    else:
        currX = (prevX ** 2) % n
        counter += 1

        xList.append(currX)

    # if duplicate X value is found, stop iterating.
    if currX == initX and counter > 0:
        return xList, counter

    return recurseBBS(n, s, xList, initX, currX, counter)


# Convert prandom X (integer) values to B (bit) values
def numToBitList(xList):
    for i in range(len(xList)):
        xList[i] = xList[i] % 2


# Recursively check if user inputed seed is relatively prime to n
def recurseCoprimeCheck(num1, num2):
    if num2 == 0:
        return num1
    else:
        return recurseCoprimeCheck(num2, num1 % num2)


# Ask user for the seed
def userInput():
    p = 11
    q = 23
    n = p * q

    while True:
        s = int(input("Input number relatively prime to " + str(n) + ": "))

        # If input seed is not relatively prime to n, ask again.
        if recurseCoprimeCheck(n, s) == 1:
            break
        else:
            print("Not relatively prime!")

    # Find the prandom X values (xList) and the period (period) of it
    xList, period = recurseBBS(n, s)

    # Comment out the line below to return the X values and not the B ones.
    numToBitList(xList)

    print("prandom bits: " + str(xList))
    print("Period: " + str(period))

    return period


userInput()
