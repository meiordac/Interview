import itertools
def permutation(n, v):
  x= list(itertools.permutations(v))
  return x[n]

print (permutation(1,[1,2,3]))