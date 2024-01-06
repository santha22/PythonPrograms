def findMax(g, n, m, col):
    maxi = -1
    ind = -1
    for i in range(n):
        if maxi < g[i][col]:
            maxi = g[i][col]
            ind = i
    
    return ind



def findPeakGrid(g: [[int]]) -> [int]:
    # Write your code here.
    n = len(g)  
    m = len(g[0])
    l, h = 0, m - 1

    while l <= h:
        mid = (l + h) // 2

        row = findMax(g, n, m, mid) 

        left = g[row][mid - 1] if (mid - 1 >= 0) else -1
        right = g[row][mid + 1] if (mid + 1 < m) else -1

        if g[row][mid] > left and g[row][mid] > right:
            return [row, mid]

        elif g[row][mid] < left:
            h = mid - 1

        else: 
            l = mid + 1
