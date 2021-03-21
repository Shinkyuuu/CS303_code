# Find a number raised to a powe of 2 while modulating it every step.
def powMod(a, c, iterator, counter=0):
    if  counter >= iterator:
        return a
   
    num1 = (a ** 2) % c

    # Print the outcome of every iteration
    # (Program runs faster when commented out)
    print("Iteration: " + str(counter + 1) + " is " + str(num1))

    return powMod(num1, c, iterator, counter+1)


# If the c isn't a power of 2, split it into powers of 2 and multiply results together.
def factorPow(a, c, bList):
    #bigPow = number raised to the power of powers of 2 multiplied together.
    bigPow = 1

    # For the length of the binary list, raise a to the power of 2 as many
    # times as its index..
    for i in range(len(bList)):
        if  bList[i] != 0:
            bigPow = (bigPow * powMod(a, c, i)) % c
            print()
    return bigPow


# Values are inputted and formatted into something more workable.
def userInput():
    # a = number to be exponentiated and modulated.
    # b = the power.
    # c = the moduli.
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    # If a binary number is converted into a list and then reversed, the powers of 
    # 2 that correspond to the binary number are equal to the index of each 
    # element in the list.
    bList = [int(i) for i in str(bin(b))[2:]]
    bList.reverse()
    finalNum = factorPow(a, c, bList)

    return finalNum


print("Solution is " + str(userInput()))

