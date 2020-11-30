##from bisect import bisect_left
##
##def BinarySearch(item_list, x):
##    i = bisect_left(item_list, x)
##    if i != len(item_list) and item_list[i] == x: 
##        return i

def BinarySearch(list_of_film_classes, like, ub, lb=0):
    mid = lb+(ub-lb)//2
    if lb>ub:
        return None
    if ub-lb == 1:
        return BinarySearch(list_of_film_classes, like, ub, mid+1)
    
    if list_of_film_classes[mid].title.lower() == like:
        return list_of_film_classes[mid].id

    elif list_of_film_classes[mid].title.lower() > like:
        return BinarySearch(list_of_film_classes, like, mid-1, lb)
    
    elif list_of_film_classes[mid].title.lower() < like:
        return BinarySearch(list_of_film_classes, like, ub, mid+1)
