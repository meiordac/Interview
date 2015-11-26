from random import randint
def Sum_prime_numbers(N):
  sp=0
  for i in range(2,N+1):
    if isProbablyPrime(i):
      sp+=i
  return sp%256

def isProbablyPrime(n, k = 2):
  if (n < 2 ):
    return False
  if n%2==0 and n!=2:
    return False
  output = True
  for i in range(0, k):
    a = randint(1, n-1)
    if (pow(a, n-1, n) != 1):
      return False 
  return output

print (Sum_prime_numbers(50))