n=int(input('enter the value of n:'))
fact=1
if n>=1:
    for i in range(1, n+1):
        fact=fact*i
print('factorial of given number is',fact)