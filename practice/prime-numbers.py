# Script text here


def getNumberOfPrimes(num):
    arr = []
    counter = 0
    numberOfPrimes = 0
    for i in range(1,num):
        counter = 0
        for j in range(1,i):
            if i%j == 0:
                counter = counter + 1
        if counter == 0:
            numberOfPrimes = numberOfPrimes  + 1
    return numberOfPrimes
    


#numberN = raw_input('Whats N: ')
numberN = 12
print getNumberOfPrimes(numberN)​