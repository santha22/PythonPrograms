class Solution:

    # arr[] : the input array
    # N : size of the array arr[]

    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, N):
        # code here
        maph = set()

        for i in arr:
            maph.add(i)

        longest = 0

        for num in maph:

            if (num - 1) not in maph:
                length = 0

                while (num + length) in maph:
                    length += 1

                longest = max(length, longest)

        return longest

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findLongestConseqSubseq(arr, n))
