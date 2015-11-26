def HackIt(str):
  result=""
  for s in str:
    if (ord(s) < 90 and ord(s)>65):
      result+=chr(90-ord(s)+65)
      
    elif (ord(s)<122 and ord(s) >97):
      result+=chr(122-ord(s)+97)
    else:
      result+=s
  return result
  
print(HackIt("XlwvUrtsgh 69"))