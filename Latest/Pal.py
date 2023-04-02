#program to check palindrome by slicing

s=input("enter the string to rev: ")

s1=s[::-1]

print("rev of the string is ",s1)

if s==s1:

  print("palindrome")

else:

  print("not palindrome")
