def notLucky(N):
  pos=1
  for i in range(1,N+1):
    if isunLucky(i):
      pos+=1
  return pos

def isunLucky(N):
  if N%13!=0:
    return False
  while N>0:
    if N%10!=7 and N%10!=4:
      return True
    N/=10
  return False

print notLucky(20)
print notLucky(100)