def divideFactorial(X, Y):
  A=X**Y
  global factors
  factors= array.array('I', [0]) * ((A + 31) // 32)
  factors[0]=1
  i=1
  while i < A+1:
    if f(i)%A==0:
      return i
    i+=1
    
  
def f(N):
  if N==1:
    return 1
  else:
    if factors[N]!=0:
      return factors[N]
    else:
      fact=f(N-1)*N
      factors[N]=fact
      return fact
  
  
print divideFactorial(1000000000,30000)