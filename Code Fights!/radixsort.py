def radixSort(a,n,maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/10**x)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

if __name__ == "__main__":
    import random
    import timeit
    a = [random.randint(0,10000) for i in xrange(1000000)]
    t = timeit.Timer('radixSort(a, 10, 5)', 'from __main__ import radixSort, a')
    print t.timeit(number=1)
