def missingK(vec: List[int], n: int, k: int) -> int:
    # Write your code here.
    l,h = 0, n - 1
    while l <= h:
        mid = (l + h) // 2

        missing = vec[mid] - mid - 1

        if missing < k:
            l = mid + 1

        else:
            h = mid - 1

    return h + k + 1
