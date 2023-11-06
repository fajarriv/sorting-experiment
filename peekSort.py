# Adopted from https://github.com/sebawild/nearly-optimal-mergesort-code/tree/master/src/wildinter/net/mergesort
def peekSortRecursive(A, left, right, leftRunEnd, rightRunStart, B):
    if leftRunEnd == right or rightRunStart == left:
        return A

    mid = left + ((right - left) // 2)
    if mid <= leftRunEnd:
        peekSortRecursive(A, leftRunEnd + 1, right, leftRunEnd + 1, rightRunStart, B)
        mergeRuns(A, left, leftRunEnd + 1, right, B)
    elif mid >= rightRunStart:
        peekSortRecursive(A, left, rightRunStart - 1, leftRunEnd, rightRunStart - 1, B)
        mergeRuns(A, left, rightRunStart, right, B)
    else:
        i = extendWeaklyIncreasingRunLeft(A, mid, left if left == leftRunEnd else leftRunEnd + 1)
        j = extendWeaklyIncreasingRunRight(A, mid, right if right == rightRunStart else rightRunStart - 1)
        if i == left and j == right:
            return A
        if mid - i < j - mid:
            peekSortRecursive(A, left, i - 1, leftRunEnd, i - 1, B)
            peekSortRecursive(A, i, right, j, rightRunStart, B)
            mergeRuns(A, left, i, right, B)
        else:
            peekSortRecursive(A, left, j, leftRunEnd, i, B)
            peekSortRecursive(A, j + 1, right, j + 1, rightRunStart, B)
            mergeRuns(A, left, j + 1, right, B)

def mergeRuns(A, l, m, r, B):
    m -= 1
    B[l:m + 1] = A[l:m + 1]
    B[m + 1:r + 1] = A[r:m:-1] + [A[m]]
    
    i, j = l, r
    for k in range(l, r + 1):
        if B[j] < B[i]:
            A[k] = B[j]
            j -= 1
        else:
            A[k] = B[i]
            i += 1

def extendWeaklyIncreasingRunLeft(A, i, left):
    while i > left and A[i - 1] <= A[i]:
        i -= 1
    return i


def extendWeaklyIncreasingRunRight(A, i, right):
    while i < right and A[i + 1] >= A[i]:
        i += 1
    return i



def peekSort(array):
    left = 0
    right = len(array) - 1
    n = right - left + 1
    peekSortRecursive(array, left, right, left, right, [0] * n)
    return array

