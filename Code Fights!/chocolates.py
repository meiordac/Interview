def Chocolates(B, w):
  chocolates=B
  tr=B
  while tr>=w:
    chocolates+=tr/w
    tr=tr%w+tr/w
  return chocolates

print(Chocolates(8932434,22))