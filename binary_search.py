from bisect import bisect_left

def BinarySearch(item_list, x):
    i = bisect_left(item_list, x)
    if i != len(item_list) and item_list[i] == x: 
        return i
