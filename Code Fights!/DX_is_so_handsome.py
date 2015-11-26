def DX_is_so_handsome(N):
  c=0
  for i in range(1,N/2+1):
    c+=DX_is_handsome(i,c)
  return c+1
    
    
def DX_is_handsome(l,c):
  if l>1:
    for j in range(1,l/2+1):
      c+=1
      DX_is_handsome(j,c)
    return c
  else:
    return 0
  
    
print(DX_is_so_handsome(8))
    
