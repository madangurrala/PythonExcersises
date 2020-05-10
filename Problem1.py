x,y=0,1
Odd_Sum = 0
FibArray = [0, 1]

while y<22:
    x,y = y,x+y
    FibArray.append(y)

Odd_Sum = sum(n for n in FibArray if n % 2)

print(Odd_Sum)
