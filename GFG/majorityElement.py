#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here 
        dict = {}
        for i in range(N):
            if A[i] in dict:
                dict[A[i]] += 1
            else:
                dict[A[i]] = 1
         
        for i in dict:
            if dict[i] > N//2:
                return i
        return -1

def main():
    T = int(input())
    while(T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.majorityElement(A,N))
        T -= 1

if __name__ == "__main__":
    main()
            
        
