def merge_sort(arr):
    """
    Merge sort implementation
    """
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    first = merge_sort(arr[:mid])
    second = merge_sort(arr[mid:])
    i, j = 0, 0
    result = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    while i < len(first):
        result.append(first[i])
        i += 1
    while j < len(second):
        result.append(second[j])
        j += 1
    return result

