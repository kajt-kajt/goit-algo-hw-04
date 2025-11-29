def insertion_sort(arr):
    """
    Insertion sort implementation
    """
    n = len(arr)
    for i in range(1,n):
        curr_element = arr[i]
        j = i -1
        while j>=0 and curr_element<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr_element

