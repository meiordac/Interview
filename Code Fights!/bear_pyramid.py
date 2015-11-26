def bear_pyramid(N):
  currentLine=0
  height=0
  while N>currentLine:
    currentLine+=1
    N-=currentLine
    height+=1
  if height>0:
    return height*3+1
  return 0
    
print (bear_pyramid(6))
