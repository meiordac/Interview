def yTimes(A):
  D={}
  for a in A:
    D[a]=0
  for a in A:
    D[a]+=1
  l=list(D.values())
  if l.count(l[0])==l.count(l[-1]):
    o=l.count(l[0])
  elif l.count(l[-1]) == l.count(l[-2]):
    return list(D)[0]
  else:
    return list(D)[-1]
  print D
  print l
  for i in range(1,len(D)):
    if o!=l.count(l[i]):
      return list(D)[i]
    o=l.count(l[i])
    print o
  return -1
    
print(yTimes([20,13,20,15,20,18,20]))