class Solution:
    def nextPermutation(self, arr, n):
        if(n<=2):
            return arr[::-1]

        pointer = n-2
        while(pointer >= 0 and arr[pointer] >= arr[pointer+1]):
            pointer -= 1

        if(pointer == -1):
            return arr[::-1]

        for i in range(n-1, pointer, -1):
            if(arr[pointer] < arr[i]):
                arr[pointer], arr[i] = arr[i], arr[pointer]
                break
        arr[pointer+1:] = reversed(arr[pointer+1:])
        return  arr

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.nextPermutation(arr, n))