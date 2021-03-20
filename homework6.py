def powMod(a, c, iterator, counter=0):
    if  counter >= iterator:
        return a
   
    num1 = (a ** 2) % c

    #print("Iteration: " + str(counter + 1) + " is " + str(num1))

    return powMod(num1, c, iterator, counter+1)


def factorPow(a, c, binList):
    bigPow = 1

    for i in range(len(binList)):
        if  binList[i] != 0:
            bigPow = (bigPow * powMod(a, c, i)) % c
            #print()
    return bigPow

def userInput(a, b, c):
    binList = [int(i) for i in str(bin(b))[2:]]
    binList.reverse()
    finalNum = factorPow(a, c, binList)

    return finalNum


print(userInput(243432243324234523254634576783456784523678456257656565654345345346765789678678678567454345234423437456327845623784567328645475745, 994326745675439687435768345786437643578643578634578643554768435786345786345786345678345786345897439943432243234234234234324342324999, 54234233244322432678324786234768324786343243423243242344))

#print((999999 ** 999999) % 23)