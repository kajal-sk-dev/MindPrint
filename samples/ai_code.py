# ai code sample - merge sort optimized

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    return merge(L,R)

def merge(L,R):
    res = []
    i=j=0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i]); i+=1
        else:
            res.append(R[j]); j+=1
    res.extend(L[i:]); res.extend(R[j:])
    return res

print(merge_sort([38,27,43,3,9,82,10]))
