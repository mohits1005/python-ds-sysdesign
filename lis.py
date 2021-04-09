## 1, 4, 8, 13
## 5
def bs(A, val):
    start = 0
    end = len(A)-1
    if val < A[0]:
        return 0
    if val > A[len(A)-1]:
        return len(A)-1
    while start <= end:
        mid = int((start+end)/2)
        if val == A[mid]:
            return mid
        elif val > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

A = [1,4,6,13, 16, 27, 50, 100]
ans = bs(A,15)
print(ans)

# A = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
# dp = [A[0]]
# for i in range(1, len(A)):
#     if dp[len(dp)-1] < A[i]:
#         dp.append(A[i])
#     else:
#         index  = bs(dp, A[i])
#         dp[index] = A[i]
# print(dp)