a = [31,29,19,7,23,13,17,5,3,11]
def heapSize():
    return len(a)
def insertObject(x):
    a.append(x)
def maxValue():
    return a[0]
def xMax():
    maxVal=a[0]
    del a[0]
    return maxVal
def heapify(j):
    j=j+1
    m=-1
    left=j*2
    right=j*2+1
    
    if  left<heapSize() and a[j] < a[left]:
        m=left
    else:
        m=j
    if  right<heapSize() and a[j] < a[right]:
        m=right
    if m!=j:
        dad=a[j]
        a[j]=a[m]
        a[m]=dad
        heapify(m)
        print m
        
    

insertObject(69)
heapify(0)
print a
