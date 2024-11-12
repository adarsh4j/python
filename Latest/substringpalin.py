Question 1
Given a string
If the string contain palindrome of length 4 increase score value by 5
If the string contain palindrome of length 5 increase the score value by 10 Initially score is 0

For example
Input string : ABABAAAA
Output : 15

Explanation :
“ABABA”AAA palindrome of length 5 (now score = 10)
ABAB“AAAA” palindrome of length 4(now score = 10+5=15)




def is_palindrome(substring):
    return substring==substring[::-1]

def check(s):
    score=0
    n=len(s)
    for i in range(0,n):
        for j in range(i+1,n+1):
            substring=s[i:j]
            if(len(substring) == 4 and is_palindrome(substring)):
                score+=5
            elif(len(substring)== 5 and is_palindrome(substring)):
                score+=10
    return score

s=input("Enter the string: ")
score=check(s)
print("Score is ",score)
