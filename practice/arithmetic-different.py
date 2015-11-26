# Script text here


def findDifferent(arr):
    diffs=[]
    finArr=[]
    numDiff=0
    for i in range(0,len(arr)-1):
        diffs.append(arr[i+1]-arr[i])
    for j in arr:
        if arr.count(j) > 1:
            numDiff=j
    print numDiff
    for i in range(0,len(arr)+1):
        finArr.append(arr[0] + numDiff)
    return finArr
        
            

array = [1,3,5,9,11]
print findDifferent(array)
​