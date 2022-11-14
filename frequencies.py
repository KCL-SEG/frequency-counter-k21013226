"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

#produces dictionary based on items list
#each item in items must contain a key
#if item is not a string then the key = item converted to string
#value = positive integer counting the no of times the item represented by key occurs in items


def frequencies(items):
    frequencies = {}

    #iterate through each element in items
    #for each item check if string if not convert

    #check dictionary is key appears
    #if it does not than add key with value 1
    #if it does then update the dictionary value by 1

    itemElement = ""

    for x in items:
        if type(items[x]) != str:
            itemElement = str(items[x])
            print("no string")
        else:
            itemElement = items[x]
            print("string")

        for y in frequencies:
            if itemElement == frequencies[y]:
                ElementCount = frequencies.get(y) + 1
                frequencies.update({itemElement,ElementCount})
                print(frequencies[x])
            else:
                frequencies[items[x]] = 1
                print(frequencies[x])



    return frequencies
