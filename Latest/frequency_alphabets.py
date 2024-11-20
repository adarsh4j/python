Question: Write a program to find the frequency of each alphabet in a given string.


def freq_string(s):
    freq={}
    for char in s:
        if char.isalpha():
          freq[char]=freq.get(char,0)+1
    return freq

s=input("Enter the string: ")
frequency=freq_string(s)
print("Frequency is ",frequency)
