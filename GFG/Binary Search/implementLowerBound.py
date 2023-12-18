def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    l,h = 0,n - 1

    
    last = n
    while l <= h:
        mid = (l + h) // 2

        if arr[mid] >= x:
            last = mid
            h = mid - 1

        else:
            l = mid + 1

    return last
