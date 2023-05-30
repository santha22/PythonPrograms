

def find(arr,n,x):
    left=binSearch(arr, x, True)
    right=binSearch(arr, x, False)
    return left, right
def binSearch(nums,target,leftBias):
    l,r=0,len(nums)-1
    i=-1
    while l<=r:
        m=(l+r)//2
        if target>nums[m]:
            l=m+1
        elif target<nums[m]:
            r=m-1
        else:
            i=m
            if leftBias:
                r=m-1
            else:
                l=m+1
    return i


t=int(input())
for i in range(t):
    n=int(input())
    x=int(input())
    arr=[int(x) for x in input().strip().split()]
    ans=find(arr,n,x)
    print(*ans)
