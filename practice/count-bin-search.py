
def findCount(number):
  arr=[1,3,5,6,7,9,13,13,13,20,25,28,39,41,46,49,50,55,55,55,55,69,70,74,78,84,84,84,91,93,95,99,100]  
  
  if findFirst(number,arr, False) == -1:
    number_of_times = 0
  else:
    number_of_times = findFirst(number,arr, False) -  findFirst(number,arr, True) + 1
    
  return number_of_times


def findFirst(number, arr, searchFirst):
  
  low = 0
  high = len(arr)-1
  
  result = -1
  
  while low<=high:
    
    med = (low + high)/2
    
    if arr[med] == number:
      result = med
      if searchFirst is True:
	high = med - 1
      else:
	low = med + 1
      if arr[low] == number:
	med = med - 1
    elif number < arr[med]:
      high = med - 1
    else: 
      low = med + 1
    
  return result

  
print findCount(13)
print findCount(55)
print findCount(84)
print findCount(200)