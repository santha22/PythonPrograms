class Solution:
    def subarr(self, arr, k):
        if(len(arr) < k):
            return arr

        i,j = 0,0
        dict = {}
        resLen = float("-infinity")
        res = [-1, -1]

        while(j < len(arr)):

            dict[arr[j]] = 1 + dict.get(arr[j], 0)

            if(len(dict) > k):
                dict[arr[i]] -= 1
                if(dict[arr[i]] == 0):
                    dict.pop(arr[i])
                i+=1

            if(len(dict) == k):
                if(j - i + 1 >= resLen):
                    res = [i, j]
                    resLen = j - i + 1

            j+=1

        if(len(res) != 0):
            i, j = res
            return arr[i:j+1]
        else:
            return arr

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.subarr(arr, k))


