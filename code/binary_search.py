def binary_search(list_of_film_classes, like, ub, lb=0):
    mid = lb + (ub - lb) // 2
    # If the lower bound is greater than upper bound then the item doesnt exist in the list
    if lb > ub:
        return None
    # When ub-lb = 1 the first item will always be chosen.
    # This condition forces the list to chose the next item
    elif ub - lb == 1:
        if list_of_film_classes[ub].title.lower() == like:
            return ub

        elif list_of_film_classes[lb].title.lower() == like:
            return lb

    elif list_of_film_classes[mid].title.lower() == like:
        return mid  # Item found with this ID

    elif list_of_film_classes[mid].title.lower() > like:
        return binary_search(list_of_film_classes, like, mid - 1, lb)

    elif list_of_film_classes[mid].title.lower() < like:
        return binary_search(list_of_film_classes, like, ub, mid + 1)
