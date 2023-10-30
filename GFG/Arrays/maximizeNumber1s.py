def findZeroes(arr, n, m) :
    # code here
    leftw, rightw = 0, 0
    zeros = 0
    maxi = 0
    
    while leftw < n and rightw < n:
        if zeros <= m:
            if arr[rightw] == 0:
                zeros += 1
            rightw += 1
            
        if zeros > m:
            if arr[leftw] == 0:
                zeros -= 1
            leftw += 1
            
        if rightw - leftw > maxi and zeros <= m:
            maxi = rightw - leftw
            
    return maxi
