for k in range(1, 1001):
    numberToProcess = k
    listOfNumbers = list()
    while numberToProcess != 0:
        listOfNumbers.append(numberToProcess % 10)
        numberToProcess = numberToProcess // 10
    sumOfDigits = 0
    for i in listOfNumbers:
        sumOfDigits += i ** len(listOfNumbers)
    if sumOfDigits == k:
        print("{}, n={}".format(k, len(listOfNumbers)))
