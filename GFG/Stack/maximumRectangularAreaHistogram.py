class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,arr):
        #code here 
        s = [-1] 

        n = len(arr) 

        area = 0

        i = 0

        left_smaller = [-1]*n 

        right_smaller = [n]*n 

        while i < n: 

            while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]): 

               right_smaller[s[-1]] = i 

               s.pop() 

            if((i > 0) and (arr[i] == arr[i-1])): 

               left_smaller[i] = left_smaller[i-1] 
 
            else: 

               left_smaller[i] = s[-1] 

            s.append(i) 

            i += 1

        for j in range(0, n): 

            area = max(area, arr[j]*(right_smaller[j]-left_smaller[j]-1)) 

        return area 
