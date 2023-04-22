
def binary_search(arr, start, end, n):

    mid = int((start+end)/2)
    if start < end:
        return False
    if arr[mid] == n:
        return True
    elif arr[mid] > n:
        return binary_search(arr, start, mid-1, n)
    elif arr[mid] < n:
        return binary_search(arr, mid+1, end, n)

a = [1,2,3,4,5,6,7,8,9]

print(binary_search(a, 0, len(a), 10))





