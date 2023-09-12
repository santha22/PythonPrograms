lass Solution:
    def isPerfectNumber(self, n):
        # code here 
        if(n <= 0):
            return 
        
        l = set()
        i = 1
        while(i*i <= n):
            if(n%i == 0):
                l.add(i)
            i+=1
        
        while(i >= 1):
            if(n%i == 0):
                l.add(n//i)
            i -= 1
        
        l = list(l)
        l.sort()
        length = len(l)
        sum = 0
        
        for i in range(length-1):
            
            sum += l[i]
            
        
        if(sum == n):
            return 1
        else:
            return 0
