def MergeArrays(A, B):
  C=[]
  for a in A:
    if a not in B and a not in C :
      C.append(a)
  for b in B:
    if b not in C:
      if b not in A:
	C.append(b)
      if b in A and A.count(b)==B.count(b):
	C.append(b)
  return sorted(C)

print(MergeArrays([10,10,10,15,20,20,25,25,30,7000],[10,15,20,20,27,7200]))