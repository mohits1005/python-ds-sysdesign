'''
Write a function that takes in non-empty array of arbitary intervals, merges any overlapping interval and returns the new interval in no particular order.

Each interval is an array of two integers, with interval[0] as start interval and interval[1] as end interval.

Note that back-to-back intervals arent considered to be overlapping. For example, [1, 5] and [6, 7] arent overlapping.
However, [1, 6] and [6, 7] are overlapping

Also, any start of interval will be less than the end of the same interval.

Input:
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

Ountput:
[[1, 2], [3, 8], [9, 10]]  # merge intervals [3, 5] [4, 7] and [6, 8]

cases to handle

1,2 : 1,3 or 1,3 : 1,2
1,3: 2,5
1,5: 2,4

'''
'''
intervals = [[100,105], [1,104]]
sort 1st index, => intervals: [1,104] [100,105]
ans = [[1,104]]
ans = [[1,105]]

intervals = [[0,0],[0,1],[0,0],[0,0],[0,0]]
ans = [[0,0]] => [[0,1]],  [0,0]

[[1,2],[3,4],[5,6],[7,8]]
ans = [[1,2],[3,4]]

[[2,3],[4,5],[6,7],[1,10]]
=> [[1,10],[2,3],[4,5],[6,7]]
ans = [[1,10]]
'''
#TC O(N) + O(NlogN) = O(NlogN)
#SC O(N)
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
ans = [intervals[0]]
for i in range(1, len(intervals)):
    if intervals[i][0] == ans[len(ans)-1][0]:
        #1,2 : 1,3 or 1,3 : 1,2 case or 1,2: 1,2 case
        bigger = max(intervals[i][1], ans[len(ans)-1][1])
        ans[len(ans)-1][1] = bigger
    elif intervals[i][0] < ans[len(ans)-1][1]:
        if intervals[i][1] < ans[len(ans)-1][1]:
            # 1,5: 2,4 case=> 1,5
            pass
        else:
            #1,3: 2,5 => 1,5 or 1,5 : 2,5
            ans[len(ans)-1][1] = intervals[i][1]
    else:
        ans.append(intervals[i])
print(ans)


'''
input = [7,1,2,4,3]
output = 3


input = N numbers
5 elements
[2,1,3,4,5]
=> n-1 elements
calculate sum of existing elements => O(N)
first n elements, Sn = n/2(2*start+(n-1)*1) = n(n+1)/2
[2,1,4,5]

'''