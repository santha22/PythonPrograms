def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    i,j = 0, 0
    flag = 0
    ans = []
    while i < n and j < m:
        if arr[i] == brr[j]:
            flag = 1
            ans.append(arr[i])
            i += 1
            j += 1

        else:
            if arr[i] < brr[j]:
                i += 1
            
            else:
                j += 1
    
    if flag == 0:
        return []

    return ans
