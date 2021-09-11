for k in range(1, 1001):
    n = 0
    numberToProcess = k
    listOfNumbers = list()

    while numberToProcess != 0:
        listOfNumbers.append(numberToProcess % 10)
        numberToProcess = numberToProcess // 10
        n += 1

    sumOfDigits = 0
    for i in listOfNumbers:
        sumOfDigits += i ** n
    if sumOfDigits == k:
        print("{}, n={}".format(k, n))