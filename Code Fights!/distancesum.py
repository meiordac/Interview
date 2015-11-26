def distancesum(n, xcor):
  dist=0
  for i in range(n):
    for j in range(i+1,n):
      dist+=((xcor[i]-xcor[j])**2)**0.5
      print dist
  return dist

print(distancesum(3,[-3,4,-3]))