def Luckynumber(N):
  pos=0
  for i in range(1,N+1):
    if isLucky(i):
      pos+=1
      print i
  return int(pos)

def isLucky(N):
  while N>0:
    if N%10!=7 and N%10!=4:
      return False
    N/=10
  return True

print (Luckynumber(4))