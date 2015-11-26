
def binarySearch(number):
  arr=[1,3,5,6,7,9,13,15,17,20,25,28,39,41,46,49,50,53,55,58,67,69,70,74,78,82,84,86,91,93,95,99,100]
  
  low = 0
  high = len(arr)-1
  
  while low<=high:
    
    med = (low + high)/2
    
    if arr[med] == number:
      return med
    elif number < arr[med]:
      high = med - 1
    else: 
      low = med + 1
    
  return -1
  
print binarySearch(41)
print binarySearch(42)
print binarySearch(69)
print binarySearch(81)