class Solution:
    def print_divisors(self, n):
        # code here
        i = 1
        l = set()
        while(i*i < n):
            if(n%i == 0):
                l.add(i)
            i += 1
        
        while(i >= 1):
            if(n%i == 0):
                l.add(n//i)
            i -= 1
            
        l = list(l)
        l.sort()
        for res in l:
            print(res, end=" ")
