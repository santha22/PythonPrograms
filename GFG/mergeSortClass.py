
class MergeSort:
    def merge_sort(self,array):
        if len(array) > 1:
            m = len(array)//2
            left = array[:m]
            right = array[m:]

            self.merge_sort(left)
            self.merge_sort(right)
            self.merge(array,left,right)
    def merge(self,array,left,right):
            i = 0
            j = 0
            k = 0
            a = len(left)
            b = len(right)
            while i < a and j < b:
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

x = MergeSort()
arr = [3,5,6,2,1,4,10,9,8,7]
x.merge_sort(arr)
print(arr)