def Cover(n):
  arr=[9]*n
  f=[False]*4
  counter=0
  for i in arr:
    j=i
    while j >0:
      if f[0]==False and j==1:
        f[0]=True
      elif f[0] == True and f[1]==False and j==9:
        f[1]=True
      elif f[1]==true and f[2]==False and j==9:
        f[2]=True
      else f[3]==False and j==8:
        f[3]=True
        counter+=1
        
        
print Cover()