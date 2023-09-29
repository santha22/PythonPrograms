from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
def f(i, j, grid, dp):
    if i == 0 and j == 0:
        return grid[0][0]

    if i < 0 or j < 0:
        return float("inf")

    if dp[i][j] != 0:
        return dp[i][j]

    up = f(i - 1, j, grid, dp) + grid[i][j]
    left = f(i, j - 1, grid, dp) + grid[i][j]
    dp[i][j] = min(up, left)
    return dp[i][j]

def minSumPath(grid):
    # Write your code here.
    n = len(grid)
    m = len(grid[0])
    dp = [[0]*m for i in range(n)]
    return f(n-1,m-1,grid, dp)

# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1