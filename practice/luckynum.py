def LuckyNum(L, R):
  n=-1
  for i in range(L,R+1):
    n=i
    while i:
      d = i % 10
      if d != 4 and d != 7:
	n=-1
      i = i / 10
    if n>0:
      return n
  return -1
  

print(LuckyNum(8,50))