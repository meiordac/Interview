def pSub(x):
  sub=''
  pal=1
  for i in range(0,len(x)):
    for j in range (i, len(x)):
      sub=x[i:j]
      if sub==sub[::-1] and i!=j :
        pal+=1
  return pal

print(pSub("abaaac"*10))
        