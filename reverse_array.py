

def reverseInGroups(arr, N, K):
    if len(arr) == N:
        arr.sort()
        arr.reverse()
        rl = arr[-K:] + arr[-N:-K]
        return rl
arr = [99,45,8,10,9]
k = reverseInGroups(arr, N=5, K=3 )

print(k)
