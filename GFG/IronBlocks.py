class Solution:
    def nBlocks(self, w):
        result = []
        binary = bin(w)[:1:-1]
        for i in range(len(binary)):
            if int(binary[i]):
                result.append(2**i)
        length = len(result)
        return length

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        w = int(input())
        obj = Solution()
        res = obj.nBlocks(w)
        print(res)