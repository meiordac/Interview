mirr=0
def mirrors(st):
  sx=-1
  sy=-1
  ex=-1
  ey=-1
  wasHere=[]
  for row in range(len(st)):
    new=[]
    for col in range(len(st[row])):
      new.append(False)
      if st[row][col]==-1:
	sx=col
	sy=row
      elif st[row][col]==-2:
	ex=col
	ey=row
    wasHere.append(new)
  solveRecursive(st,wasHere,sx,sy,ex,ey)
  return mirr

def solveRecursive(st,wh,x,y,ex,ey):
  if x==ex and y==ey:
    return 0
  if st[x][y]==1:
    return 0
  if wh[h][y]==False:
    if x!=0 and st[x-1][y]>0:
      mirr+=st[x-1][y]
    if x!=len(st[y]-1) and st[x+1][y]>0:
      mirr+=st[x+1][y]
    if y!=0 and st[x][y-1]>0:
      mirr+=st[x][y-1]
    if y!= len(st) and st[x][y+1]>0:
      mirrors+=st[x][y+1]
  wh[x][y]=True
  if x!=0:
    solveRecursive(st,wh,x-1,y,ex,ey)
  if x!=len(st[y]):
    solveRecursive(st,wh,x+1,y,ex,ey)
  if y!=len(st):
    solveRecursive(st,wh,x,y+1,ex,ey)
  if y!= 0:
    solveRecursive(st,wh,x,y-1,ex,ey)
  
  
  return 0
  
  
	

print(mirrors( [[1,-1,1,1,1],
 [1,0,0,0,1],
 [1,0,1,1,1],
 [1,0,0,0,1],
 [1,1,1,0,1],
 [0,0,1,0,1],
 [0,0,1,-2,1]] ))