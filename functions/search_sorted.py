def searchsorted(arr, val, side='left'):
    low = 0
    high = len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < val or (side == 'right' and arr[mid] == val):
            low = mid + 1
        else:
            high = mid
    return low
