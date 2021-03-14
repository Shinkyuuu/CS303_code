# Add pseudorandom (prandom) integer values to a list until the period is complete
def bbs(n, s):
    # xList = list in which the prandom integers will be added to.
    # initX = initial X value.
    # currX = current prandom X value.
    # counter = added to by 1 every iteration, inevitably becomes the period.
    xList = []
    currX, initX = 0, 0
    counter = 0

    while True:
        currX = (s ** 2) % n
        s = currX

        if counter == 1:
            initX = currX
        elif initX == currX:
            break

        if counter > 0:
            xList.append(currX)
            
        counter += 1

    return xList, counter-1


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
    p = 211
    q = 719
    n = p * q

    while True:
        s = int(input("Input number relatively prime to " + str(n) + ": "))

        # If input seed is not relatively prime to n, ask again.
        if recurseCoprimeCheck(n, s) == 1:
            break
        else:
            print("Not relatively prime!")

    # Find the prandom X values (xList) and the period (period) of it
    xList, period = bbs(n, s)

    # Comment out the line below to return the X values and not the B ones.
    #numToBitList(xList)

    print("prandom bits: " + str(xList))
    print("Period: " + str(period))

    return period


userInput()
