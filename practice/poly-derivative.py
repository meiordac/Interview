

def derivative(poly):
  poly_der=''
  degree = -1
  for j in poly:
    coef = int(j)*(degree+1)
    poly_der = poly_der + str(j)[0]+str(coef)+'x**'+str(degree)
    degree = degree + 1
    
  print poly_der
  

polynomial = []

pol_str= raw_input('polynomial? ')
polynomial=pol_str.split(',')

print 'your poly is: '
coef = 0

poly_org=''

for p in polynomial:
  poly_org = poly_org + p+'x**'+str(coef)
  coef=coef+1
  
print poly_org
  
derivative(polynomial)
