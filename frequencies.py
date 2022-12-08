def frequencies(items):
    frequencies = {}
    newList = []
    for item in items:
        newList.append(f"{item}")

    for item in newList:
        frequencies.update({item : newList.count(item)})


    print(frequencies)    
    return frequencies
