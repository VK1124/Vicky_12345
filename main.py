# 1.1 implement a recursive function to calculate the factorial of given number .

"""
1! =1 Ã— 1
2! = 2 Ã— 1!--->2 Ã— 1
3! = 3 Ã— 2!--->3 Ã— 2 Ã— 1
.
.
10! = 10 Ã— 9! ---> 10 Ã— 9 Ã— 8 Ã—... Ã— 1

Formula - n x (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1 )

number = int(input ("Enter a value :"))
res = fact_rec(number)

print( "The factorial of {} is {}".format(number,res))