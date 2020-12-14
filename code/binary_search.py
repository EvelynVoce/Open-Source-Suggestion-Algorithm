
def BinarySearch(list_of_film_classes, like, ub, lb=0):
    mid = lb+(ub-lb)//2
    #If the lower bound is greater than upper bound then the item doesnt exist in the list
    if lb>ub:
        return None
    #When ub-lb = 1 the first item will always be chosen.
    #This condition forces the list to chose the next item
    
    elif ub-lb == 1:
        if list_of_film_classes[ub].title.lower() == like:
            return list_of_film_classes[ub].id
        
        elif list_of_film_classes[lb].title.lower() == like:
            return list_of_film_classes[lb].id
    
    elif list_of_film_classes[mid].title.lower() == like:
        return list_of_film_classes[mid].id # Item found with this ID

    elif list_of_film_classes[mid].title.lower() > like:
        return BinarySearch(list_of_film_classes, like, mid-1, lb)
    
    elif list_of_film_classes[mid].title.lower() < like:
        return BinarySearch(list_of_film_classes, like, ub, mid+1)
