n=int(input())

if(n==0 or n<0):

    print("Value is less than 1")

else:

   fact=1

   while(n):

     fact*=n

     n=n-1

   print(f"Factorial is {fact}")

   

