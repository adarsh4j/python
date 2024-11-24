
Question:
Write a Python function called longest_prefix that takes a list of strings as input and returns the longest common prefix shared by all the strings. If no common prefix exists, return an empty string.

The function should use sorting to optimize the process.

Constraints:

The input list contains at least 1 and at most 10,000 strings.
The length of each string does not exceed 200.



def longest_prefix(strings):
    if not strings:
        return ""
    strings.sort()
    first=strings[0]
    last=strings[-1]
    common_prefix=""
    for i in range(min(len(first),len(last))):
       if first[i]==last[i]:
           common_prefix+=first[i]
       else:
            break
    return common_prefix

n=int(input("Enter the number of Words : "))
strings=[input(f"Enter string {i+1} : ") for i in range(n)]
longestprefix=longest_prefix(strings)
print(longestprefix)
