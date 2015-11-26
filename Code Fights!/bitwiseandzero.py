def bitwiseandzero(n, array):
  num=0
  for i in array:
    for j in array:
      if i & j ==0 and i!=j:
        num+=1
  return num
      
print (bitwiseandzero(3,[3,6,0]))