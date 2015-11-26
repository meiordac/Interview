def DX_is_so_handsome(N):
  luckies=[]
  for i in range(N+1):
    if isLucky(i):
      luckies.append(i)
  return luckies   
    
def isLucky(N):
  while N>0:
    if not (N%10==4 or N%10==7):
      return False
    N/=10
  return True

print (DX_is_so_handsome(77))