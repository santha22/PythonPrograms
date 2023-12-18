def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    l,h = 0,n - 1
    last = n
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] <= x:
            l = mid + 1

        else:
            last = mid
            h = mid - 1
            

    return last
