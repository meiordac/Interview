
def permutation(s1,s2):
    t1=0
    t2=0
    for s in s1:
        t1=t1+ord(s)
    for d in s2:
        t2 = ord(d)+t2
    if t1 == t2:
        return True
    else:
        return False
        
print(permutation("hola","oalh"))
