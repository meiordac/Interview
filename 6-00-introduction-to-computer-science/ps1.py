pp=2
ps = [pp]
pp+=1
ps.append(pp)
while len(ps) <1000:
  pp+=2
  test = True
  for a in ps:
      if pp%a==0:
	test=False
	break
  if test:
    ps.append(pp)
      

print (ps)