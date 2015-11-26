def CountNumber(N, X):
  count=0
  for i in range(1,X):
    j=0
    while j<N+1:
      if j>X:
        break
      if i*j==X:
        count+=1
      j+=1
  return count

print CountNumber(10,5)