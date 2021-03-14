def printList(pList):
    # For every item in the list, print it
    for i in pList:
        print(''.join(i))


def permute(permWord, permList=[], count=0):
    # permWord = word to be permuted
    # permList = the list of all permutations
    # count = the index of a specific letter in permWord

    # If count equals the word's length, then there are no more letters to be added to permList
    if count == len(permWord):
        printList(permList)

        return

    # If permList is empty, add the first letter of permWord
    elif len(permList) == 0:
        permList.append(permWord[count])
        permute(permWord, permList, count + 1)

    else:
        # If at least one element is in permList, create a new list (newPermList).
        # Insert the next letter once in every index of every element  in permList and
        # append it to newPermList each time.
        #
        # Example: for word "hello"
        #           permList = [['h']],
        #           newPermList = [['e', 'h'], ['h', 'e']]
        #
        # (This process continues for every letter in "hello")
        newPermList = []

        for perm in permList:
            for i in range(0, count + 1):
                # tempPerm is used to add a letter to perm without changing it
                tempPerm = []
                tempPerm.extend(perm)
                tempPerm.insert(i, permWord[count])
                newPermList.append(tempPerm)

        # Recurse the function but newPermList becomes the new permList and count iterates to the next letter's index
        permute(permWord, newPermList, count + 1)


permute("wxyz")
