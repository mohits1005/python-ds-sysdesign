def recurse(A, dictionary):
    ans = 0
    for i in range(0, len(A)):
        prefix = A[:i]
        suffix = A[i:]
        if suffix in dictionary:
            if len(prefix) == 0:
                ans += 1
            else:
                ans += recurse(prefix, dictionary)
    return ans

dictionary = {
    "loves":1,
    "pep":1,
    "coding":1,
    "pepcoding":1,
    "ice":1,
    "cream":1,
    "icecream":1,
    "man":1,
    "go":1,
    "mango":1
}
A = "pepcodinglovesmangoicecream"
ans = recurse(A, dictionary)
print(ans)