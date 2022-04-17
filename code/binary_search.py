
def binary_search(list_of_media_objects, like, ub=None, lb=0):
    if ub is None:
        ub = len(list_of_media_objects)

    mid = lb + (ub-lb) // 2
    if lb > ub or mid == ub:
        return None

    if list_of_media_objects[mid].title.lower() == like:
        return mid

    if like < list_of_media_objects[mid].title.lower():
        return binary_search(list_of_media_objects, like, mid, lb)
    else:
        return binary_search(list_of_media_objects, like, ub, mid+1)