def bubble_sort(items):
    """
    Return array of items, sorted in ascending order,
    using the bubble sort method

    Args:
        items : list of unordered numbers

    Returns:
        list : list of elements in items in ascending order
    """
    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out

def merge_sort(items):
    """
    Return array of items, sorted in ascending order,
    using the merge sort method

    Args:
        items : list of unordered numbers

    Returns:
        list : list of elements in items in ascending order
    """

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    new_list = []
    while len(i1) > 0 and len(i2) > 0:
        if i1[0] < i2[0]:
            new_list.append(i1[0])
            i1.pop(0)
        else:
            new_list.append(i2[0])
            i2.pop(0)

    if len(i1) == 0:
        new_list = new_list + i2
    if len(i2) == 0:
        new_list = new_list + i1
    return new_list



def quick_sort(items):
    """
    Return array of items, sorted in ascending order
    using the quick sort method

    Args:
        items : list of unordered numbers

    Returns:
        list : list of elements in items in ascending order
    """
    if  len(items) <= 1:
        return items

    pivot = items[0]
    start = []
    end = []
    middle = []
    for i in items:
        if i < pivot:
            start.append(i)
        elif i > pivot:
            end.append(i)
        elif i == pivot:
            middle.append(i)

    start = quick_sort(small)
    end = quick_sort(large)

    return start + middle + end
