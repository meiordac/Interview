def getCandyPosition(N, r, c, candy):
  b=0
  rp=0
  if candy%(c*r)==0:
    b=candy/(c*r)
  else:
    b=candy/(c*r)+1
  if candy%(c*r)==0:
    rp=(c*r)
  else:
    rp=candy%(c*r)
  co=(c*r)
  print rp
  print co
  for i in range(r):
    for j in range(c):
      if co==rp and candy<=N:
        return (b,i,j)
      co-=1
  return (-1,-1,-1)
      

print (getCandyPosition(6,2,2,4))

     