

def spiraling(ma):
  tr = 0
  br = len(ma) -1
  lc = 0
  rc=len(ma[tr])-1
  dir = 0
  
  while tr <= br and lc <= rc:
    
    if dir == 0:
      for j in range(lc,rc+1):
	print ma[tr][j]    
      tr = tr + 1
      
      
    elif dir==1:
      for i in range(tr,br+1):
	print ma[i][rc]
      rc = rc -1
      
    elif dir==2:
      for j in range(rc, lc-1,-1):
	print ma[br][j]
      br = br - 1
	
    else:
      for i in range(br,tr-1,-1):
	print ma[i][lc]
      lc = lc +1
      
    dir = (dir + 1) % 4
      
matrix=[[2,5,8],[10,15,19],[21,28,35]]
print matrix
spiraling(matrix)