def merge(arr1, arr2, n, m):
    arr3 = [0]*(n+m)
    left = 0
    right = 0
    index = 0
    while(left < n and right < m):
        if(arr1[left] < arr2[right]):
            arr3[index] = arr1[left]
            index += 1
            left += 1
        else:
            arr3[index] = arr2[right]
            index += 1
            right += 1

    while(left < n):
        arr3[index] = arr1[left]
        index += 1
        left += 1

    while(right < m):
        arr3[index] = arr2[right]
        index += 1
        right += 1

    for i in range(n+m):
        if(i < n):
            arr1[i] = arr3[i]
        else:
            arr2[i-n] = arr3[i]

    for i in arr1:
        print(i, end=" ")
    for i in arr2:
        print(i, end=" ")

arr1 = [1, 2, 3, 10]
arr2 = [5, 6, 7, 8, 9]
n = len(arr1)
m = len(arr2)
merge(arr1, arr2, n, m)