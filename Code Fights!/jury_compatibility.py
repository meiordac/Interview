def jury_compability(N, M, votes):
  balance=[]
  for j in range(M):
    jurado=0
    for n in range(2):
      jurado+=votes[j][n]
    balance.append(jurado)
  for j in range(M):
    if balance[j]>0:
      return True
  return False

print(jury_compability(3,3,[[1,2],[-1,-2],[1,3]]))
