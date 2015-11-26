

findMissing(arr,n):
  difference = -1
  differences=[{'diff':-1,'count':-1}]
  for i in range(0,len(arr)):
    if arr[i+1] - arr[i] != difference:
      difference = arr[i+1] - arr[i]
      differences.append({'diff':difference,'count':1})
  print differences
  
array=[1,3,5,9,11]

findMissing(array, 5)