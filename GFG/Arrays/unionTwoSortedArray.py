
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        i = 0
        j = 0
        unionArr = []
    
        while i < n and j < m:
            if a[i] <= b[j]:
                if len(unionArr) == 0 or unionArr[-1] != a[i]:
                    unionArr.append(a[i])
                i += 1
            else:
                if len(unionArr) == 0 or unionArr[-1] != b[j]:
                    unionArr.append(b[j])
                j += 1
        
        while j < m:
            if len(unionArr) == 0 or unionArr[-1] != b[j]:
                unionArr.append(b[j])
            j += 1
        
        while i < n:
            if len(unionArr) == 0 or unionArr[-1] != a[i]:
                unionArr.append(a[i])
            i += 1
        
        return unionArr
