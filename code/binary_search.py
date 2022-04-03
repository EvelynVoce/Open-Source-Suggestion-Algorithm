def binary_search(list_of_media_objects, like, ub, lb=0):
    mid = lb + (ub - lb) // 2
    # If the lower bound is greater than upper bound then the item doesn't exist in the list
    # print(list_of_media_objects[mid].title.lower())
    # print(list_of_media_objects[ub].title.lower())
    # print(list_of_media_objects[lb].title.lower())
    if lb > ub:
        return None
    # When ub-lb = 1 the first item will always be chosen.
    # This condition forces the list to choose the next item
    elif ub - lb == 1:
        if list_of_media_objects[ub].title.lower() == like:
            return ub

        elif list_of_media_objects[lb].title.lower() == like:
            return lb

    elif list_of_media_objects[mid].title.lower() == like:
        return mid  # Item found with this ID

    elif list_of_media_objects[mid].title.lower() > like:
        return binary_search(list_of_media_objects, like, mid - 1, lb)

    elif list_of_media_objects[mid].title.lower() < like:
        return binary_search(list_of_media_objects, like, ub, mid + 1)
