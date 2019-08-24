def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        while arr[j] > arr[j+1] and j>=0:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1 
    return arr

arr=[7, 8, 5, 9, 4, 10]
print(insertion_sort(arr))
