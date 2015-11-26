def filterBible(scripture, book, chapter):
  r=[]
  for s in scripture:
    b= book in s[0:2]
    c= chapter in s[2:5]
    if not (b and c):
      scripture.remove(s)
  return r 

print (filterBible(["01001001","01001002","01002001","01002002","01002003","02001001","02001002","02001003","66022021"],"01","001"))



#["01001001","01001002"]