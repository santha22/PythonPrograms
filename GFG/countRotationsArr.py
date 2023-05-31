def count_rotations_linear(nums):
    position=0
    while position < len(nums):
        if position > 0 and nums[position] <  nums[position-1]:
            return position
        position +=1
    return 0

t=int(input())
for i in range(t):
    n=int(input())
    nums=[int(x) for x in input().strip().split()]
    print(count_rotations_linear(nums))
