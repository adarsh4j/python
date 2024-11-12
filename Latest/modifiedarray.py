Given an array. Select the alternative elements in the array starting from second position. Reverse these elements and place them in the array

For example
Input : 1 5 6 7 8 9 0
Output : 1 9 6 7 8 5 0

ANSWER:

def modify_array(arr):
    alternative_arr=arr[1::2]
    reverse_alternative=alternative_arr[::-1]
    arr[1::2]=reverse_alternative
    return arr

arr = list(map(int,input().split()))
modified_array=modify_array(arr)
print((" ".join(map(str, modified_array))))
