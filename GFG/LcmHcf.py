class Solution:
    def Gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.Gcd(b, a % b)

    def lcmAndGcd(self, A, B):
        # code here
        gcd = self.Gcd(A, B)
        lcm = (A * B) // gcd
        return lcm, gcd



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        ob = Solution()
        ptr = ob.lcmAndGcd(a,b)
        print(ptr[0],ptr[1])