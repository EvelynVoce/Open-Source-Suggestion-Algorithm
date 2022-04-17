from media_data_csv_reader import reading_csv


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


# TEST BINARY SEARCH CODE
if __name__ == "__main__":
    list_of_media_classes = reading_csv("films_data2.csv")
    list_of_media_classes.sort(key=lambda x: x.title)

    for i, y in enumerate(list_of_media_classes):
        print(i, y.title.lower())
        print(binary_search(list_of_media_classes, y.title.lower(), len(list_of_media_classes)))
