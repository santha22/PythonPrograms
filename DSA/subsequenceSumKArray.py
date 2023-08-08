def recur(index,current_subseq,arr,sum,target_sum):
    if(index == len(arr)):
        if sum == target_sum:
            print(' '.join(map(str,current_subseq)))
        return
    recur(index+1,current_subseq + [arr[index]],arr,sum+arr[index],target_sum)
    recur(index+1,current_subseq,arr,sum,target_sum)

def subsquenceSum(arr,target_sum):
    ans = []
    sum = 0
    index = 0
    recur(index,ans,arr,sum,target_sum)
    print(ans)

arr = [1,2,1]
target_sum = 2
subsquenceSum(arr,target_sum)
