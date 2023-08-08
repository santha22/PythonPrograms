class Solution:
    def generate(self, s, current_sum, target_sum, index, path, result):
        if index == len(s):
            if current_sum == target_sum:
                result.append(path)
            return
        self.generate(s, current_sum + s[index], target_sum, index + 1, path + [s[index]], result)
        self.generate(s, current_sum, target_sum, index + 1, path, result)

    def AllPossibleStrings(self, arr, target_sum):
        result = []
        current_sum = 0
        index = 0
        self.generate(arr, current_sum, target_sum, index, [], result)
        return result

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int,input().split()))
        target_sum = int(input())
        ob = Solution()
        ans = ob.AllPossibleStrings(arr,target_sum)
        for i in ans:
            print(i,end=" ")
        print()