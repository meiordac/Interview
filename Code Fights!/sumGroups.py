def SumGroups(arr):
  terminar =True
  while terminar:
    l=0
    print arr
    for i in range(1,len(arr)):
      if arr[l] % 2==0 and arr[i] % 2==0:
	arr[i]+=arr[l]
	arr.pop(l)
	break
      elif arr[l]%2!=0 and arr[i]%2!=0 :
	arr[i]+=arr[l]
	arr.pop(l)
	break
      if i == len(arr)-1:
	terminar=False
	print i
      l=i
  return len(arr)
    
    
    
print (SumGroups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]))