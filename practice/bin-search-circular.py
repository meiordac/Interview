def find_circular(arr, number):
  low=0
  high=len(arr)-1
  
  while low<=high:
    mid = (low + high)/2
    
    if arr[mid] == number: #Case 1: Found number, yeah :)
      return mid
    elif arr[mid] <= arr[high]: #Case 2 right half is sorted
      if number > arr[mid] and number <= arr[high]:
	low = mid + 1
      else:
	high = mid -1
    else: #Case 3 left side is sorted
	  if number < arr[mid] and number >= arr[low]:
	    high = mid - 1
	  else:
	    low = mid-1
  return -1
  

array =  [10,11,12,2,3,5,8]
x=raw_input('Enter a number: ')
print find_circular(array,int(x))
  