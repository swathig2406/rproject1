n=int(input('enter the value of n:'))
avg=0.0
d=0
for i in range(1,n+1):
    d=d+i
avg=d/i
print('the sum of first',n,'natural numbers is',d)
print('the average of first',n,'natural numbers is',avg)