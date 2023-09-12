

def pascal(n):
    row = n
    ans = 1
    row_elements = [1]
    for i in range(1, row):
        ans = ans * (n - i) // i
        row_elements.append(ans)
    return row_elements

n = 73
row_elements = pascal(n)
print(*row_elements)
