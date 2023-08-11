class Solution:
    def recursion(self, index, target_sum, result, A, ds):
        if(target_sum == 0):
            result.append(ds.copy())
            return

        for i in range(index,len(A)):
            if(A[i]>target_sum):
                break
            if(i>index and A[i] == A[i-1]):
                continue
            ds.append(A[i])
            self.recursion(i,target_sum-A[i],result,A,ds)
            ds.pop()


    def combinationalSum(self,A,B):
        result = []
        index = 0
        self.recursion(index,B,result,sorted(A),[])
        return result

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(",end="")
            size = len(result[i])
            for j in range(size-1):
                print(result[i][j],end=" ")
            if(size):
                print(result[i][size-1],end=")")
            else:
                print(")",end="")
        print()