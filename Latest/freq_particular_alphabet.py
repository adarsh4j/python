Write a program to find frequency of particular character in a string


def freq_string(s):
    char=input("Enter the character to find the frequency : ").strip()
    freq=0
    for c in s:
       if char==c:
           freq+=1
    return freq

s=input("Enter the string: ")
frequency=freq_string(s)
print("Frequency is the character is  ",frequency)
