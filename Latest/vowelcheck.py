Given a string
If the string contain vowels replace every character of the string with first occurring vowel, If the string does not contain a vowel return original string

For example
Input string : BOB
Output : OOO

Explanation :
First occurring vowel in the string is O
So BOB ==> OOO

def check(s):
    vowels="aeiouAEIOU"
    first_vowel=None
    for char in s:
        if char in vowels:
           first_vowel=char
           break
    if first_vowel:
        s = first_vowel * len(s)
    return s
s=input("Enter the string: ")
newstring=check(s)
print(newstring)
