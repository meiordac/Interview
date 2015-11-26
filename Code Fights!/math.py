import re
from math import sqrt
def math(e):
  o=e.split('=')[0]
  o=o.replace('^','**')
  return int(eval(o))
 
  
print(math('2+2='))# = 4
print(math('(10^3-500)/(10^2)='))# = 5
print(math('sqrt(28+8-9)='))# = 5
print(math('75*(sqrt(82)-9)='))# = 4
print(math('-5*(-5)='))# = 25
print(math('5*(-5)='))# = -25
print(math('(10^2)/10='))# = 10
