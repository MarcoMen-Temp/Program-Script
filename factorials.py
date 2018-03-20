"""Marco Men - Adapted from: "Introduction to Programming using Python"
by Y. Daniel Liang - Page Reference (Pg.501)"""

def factorial(n):
  if n==0:#Base case
     return 1
  else:
    return n*factorial(n-1)#Recursive call

print (factorial(5))
print (factorial(7))
print (factorial(10))