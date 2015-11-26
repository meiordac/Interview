 
def find_min_binary(arr):
  low = 0
  high = len(arr)-1
  min_num = high
  
  while low <= high:
    med = (low + high)/2
    
    if arr[med] < arr[high] and arr[low] > arr[med]:
      min_num = med
      break
    elif arr[med] < arr[high]:
      high = med - 1
    else:
      low = med + 1
  return min_num
      
    

def find_min(arr):
  min_num = len(arr)-1
  for pos in range(0,len(arr)-1):
    if arr[pos] < arr[min_num]:
      min_num=pos
  return min_num
  

def times_rotates(arr):
  return find_min_binary(arr)

#array = [11,12,2,3,5,8,10]
array =  [10,11,12,2,3,5,8]
print times_rotates(array)
  