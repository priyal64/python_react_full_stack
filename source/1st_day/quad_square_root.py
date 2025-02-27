# finding sqaure root of quadratic equation
#  -(b/2a) = ±√ (b2 - 4ac) / 2a
a=input("enter a value:")
b=input("enter b value:")
c=input("enter c value:")
d=int((int(b)**2-4*int(a)*int(c))**0.5)
root1=-int(b)+d
root2=-int(b)-d
print("the roots are:")
print(root1/2*int(a))
print(root2/2*int(a))
