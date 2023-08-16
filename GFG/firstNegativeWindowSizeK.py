from collections import deque
def printFirstNegativeInteger(N, K, A):
    result = []
    q = deque()
    i,j = 0,0

    while(j<N):
        if(A[j] < 0):
            q.append(A[j])

        if(j - i + 1 == K):
            if(len(q) == 0):
                result.append(0)
            else:
                result.append(q[0])
                if(A[i] == q[0]):
                    q.popleft()
            i += 1

        j += 1

    return result


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int,input().split()))
        K = int(input())
        res = printFirstNegativeInteger(N,K,A)
        print(*res)