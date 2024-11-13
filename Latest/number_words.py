Number of Words corresponding to the numbers


def number_word(n):
    words=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return words[n]
n=int(input())
result=" ".join(number_word(int(digit)) for digit in str(n))
print(result)
