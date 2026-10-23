# human code - bubble sort - i learned this in first year
# not efficient but i remember it

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # swap - i always do this temp way
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

a = [64, 34, 25, 12, 22]
print(bubble(a))
