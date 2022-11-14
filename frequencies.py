

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}

    #iterate through each element in items
    #for each item check if string if not convert
    #check dictionary is key appears
    #if it does not than add key with value 1
    #if it does then update the dictionary value by 1

    itemElement = ""

    for x in items:
        if type(x) != str:
            itemElement = str(x)

        else:
            itemElement = x

        KeyList = frequencies.keys()

        if itemElement in KeyList:
            ElementCount = frequencies.get(itemElement) + 1
            frequencies.update({itemElement:ElementCount})
            print("updated key value string")

        else:
            frequencies[itemElement] = 1
            print("added key value string")


        for x in frequencies:
            print(x)


    return frequencies
