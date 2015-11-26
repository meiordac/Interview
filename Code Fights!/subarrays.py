def CountSubArray(Array, n, d):
  for k in Array:
    respuesta=AddSub(Array,n-1,d, respuesta)
    if respuesta!=-1:
      return respuesta

def AddSub(Array,n,d,total):
  

