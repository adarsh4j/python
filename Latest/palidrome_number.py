
def is_palindrome(n):
    return n==n[::-1]

n=input()
palin=is_palindrome(n)
if palin:
    print("The number is palindrome")
else:
    print("The number is not plaindrome")
