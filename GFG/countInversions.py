class Solution:
    def merge(self, arr, l, m, r):
        i = l
        j = m + 1
        temp = []
        count = 0  # Initialize the inversion count for this merge operation
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count += (m - i + 1)  # Update the inversion count
                j += 1

        while i <= m:
            temp.append(arr[i])
            i += 1

        while j <= r:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[l + k] = temp[k]

        return count  # Return the inversion count for this merge operation

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            count = 0  # Initialize the inversion count for this mergeSort call
            count += self.mergeSort(arr, l, mid)
            count += self.mergeSort(arr, mid + 1, r)
            count += self.merge(arr, l, mid, r)
            return count
        return 0

    def inversionCount(self, arr, n):
        return self.mergeSort(arr, 0, len(arr) - 1)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(Solution().inversionCount(arr, n))
