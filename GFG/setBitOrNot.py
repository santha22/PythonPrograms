class Solution:
    def setBit(self, n, k):
        if(n & (1 << k) != 0):
            return True
        else:
            return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        k = int(input())
        ob = Solution()
        print(ob.setBit(n, k))