def KthMissingElement (arr,  n, k) : 
    #Complete the function
    i = 0
    while i < n - 1:
        diff = arr[i + 1] - arr[i]
        
        if diff > k:
            return k + arr[i]
            
        else:
            k = k - (diff - 1)
            
    return -1
    
