class Solution:
    def lemonadeChange(self, n, bills):
        # Code here
        five, ten = 0, 0
        for i in range(n):
            x = bills[i]
            if x == 5:
                five += 1
                
            elif x == 10:
                five -= 1
                ten += 1
            
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                    
                else:
                    five -= 3
            
            if five < 0:
                return False
                
        return True
