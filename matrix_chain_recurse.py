def recurse(A, i, j):
    if i == j:
        return 0
    ans = float('inf')
    for k in range(i,j):
        print('m',i,j,k)
        l = recurse(A,i,k)
        r = recurse(A,k+1,j)
        m = A[i]*A[k+1]*A[j+1]
        ans = min(ans, l+r+m)
    return ans

A = [1, 2, 3, 4, 3]
ans = recurse(A, 0, len(A)-2)
print(ans)