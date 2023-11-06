def countinSortForRadix(array, exponent):
    sizeArray = len(array)
    output = [0] * sizeArray
    count = [0] * 10

    for i in range(sizeArray):
        index = (array[i] // exponent) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = sizeArray - 1
    while i >= 0:
        index = (array[i] // exponent) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    for i in range(sizeArray):
        array[i] = output[i]

    return array

def radixSort(array):
    max_element = max(array)
    exponent = 1
    while max_element // exponent > 0:
        countinSortForRadix(array, exponent)
        exponent *= 10
    return array