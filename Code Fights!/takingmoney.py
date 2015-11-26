def TakingMoney(N, X):
  for x in range(0,N):
    if X[x]>1:
      return "ambiguous"
  return "not ambiguous"

print TakingMoney(15,[0,0,1,0,1,0,0,1,0,1,1,1,1,1,0])