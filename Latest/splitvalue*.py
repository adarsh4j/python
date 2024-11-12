Question 3
Two numbers x and y are read by user
x = a + b
y = a — b
The output is value of z = a * b

For example
Input : x = 7 , y = 1
Output : 12

Explanation :
x = 7 = 4 + 3
y = 1 = 4–3
So z = 4 * 3 = 12

Answer:

x=int(input("Enter x value : "))
y=int(input("Enter y value : "))
a=(x+y)//2
b=(x-y)//2
z=a*b
print(z)
