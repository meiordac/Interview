def Count_SubArray(Array, n, d):
  answer=0
  suma=0
  for i in Array:
    for j in Array:
      for k in Array:
	if i!=j and j!=k:
	  suma = i+j+k
	  if suma%d==0:
	    print (i,j,k)
	    answer+=1
  return answer/3
print Count_SubArray([1,2,3,4,5,6,10,20,30,1,2,5,2,0],3,5)