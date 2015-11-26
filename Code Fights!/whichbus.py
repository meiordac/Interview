def whichBusToTake(n, busesColors, goingToSchool):
  for i in range(n):
    if goingToSchool(i)==True and busesColors[i]=="red":
      return i
  for i in range(n):
    if goingToSchool(i):
      return i
      
print(whichBusToTake(3,["red","red","blue"],[True,True,True]))