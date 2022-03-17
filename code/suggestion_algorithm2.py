from media_data_csv_reader import reading_csv
import binary_search
import profiler  # This profiles the system, so I can check if anything is too inefficient
from os import system
from SearchClass import SearchData

# Defining global variables at the module level.
list_of_media_classes = []


# @profiler.profile
def suggestion_algorithm_single_use(local_media_classes, likes_to_save: list[int]):
    global list_of_media_classes
    list_of_media_classes = local_media_classes
    # This includes features that only need to be run at the start like setting saved media to seen
    data_of_index: list[str] = [data for like in likes_to_save for data in list_of_media_classes[like].get_data()]
    for like in likes_to_save:
        # Media seen checked here, not in selecting_media so media can be set to seen after program is closed
        if not list_of_media_classes[like].viewed:
            list_of_media_classes[like].set_viewed()

    return data_of_index


@profiler.profile
def suggestion_algorithm(media_data_to_set_scores):
    for each_item in list_of_media_classes:  # Compare each item with the data of the media the user likes
        each_item.set_score(media_data_to_set_scores)


def directing_to_retailer(title: str) -> str:
    amazon_link: str = "https://www.amazon.com/s?k="
    full_link: str = amazon_link + title.replace(" ", "+")
    return full_link


def selecting_media(likes_to_save, like):
    if like == "exit":
        print("exit engaged")
        return None

    # Binary Search
    list_of_media_classes.sort(key=lambda x: x.title)  # Sort by title so binary search can be performed
    found_item = binary_search.binary_search(list_of_media_classes, like.lower(), len(list_of_media_classes) - 1)
    if found_item is not None:
        # data_of_index can be a set here because duplicates aren't relevant when only one media is considered
        data_of_index: set = {iterator for iterator in list_of_media_classes[found_item].get_data()}
        list_of_media_classes[found_item].set_viewed()
        found_item_id: int = list_of_media_classes[found_item].id
        likes_to_save = max_likes(found_item_id, likes_to_save)

        amazon_link = directing_to_retailer(like)
        searched_data = SearchData(data_of_index, amazon_link)
        return searched_data, likes_to_save
    else:
        system('cls')


def max_likes(found_item_id, likes_to_save):
    # The system only keeps track of the last 100 items the user likes between sessions
    if len(likes_to_save) >= 100:
        list_of_media_classes.sort(key=lambda x: x.id)  # Needed to set the items to not viewed
        list_of_media_classes[likes_to_save[0]].set_not_viewed()
        likes_to_save.pop(0)
    likes_to_save.append(found_item_id)
    return likes_to_save


def main_algorithm(local_media_classes, media_data_to_set_scores, likes_to_save):
    global list_of_media_classes
    list_of_media_classes = local_media_classes  # 0.1 seconds roughly

    suggestion_algorithm(media_data_to_set_scores)
    list_of_media_classes.sort(key=lambda x: x.score, reverse=True)  # Efficient sorting algorithm
    return list_of_media_classes

    # searched_data = selecting_media(likes_to_save)
    # media_data_to_set_scores = searched_data.data
    # print(searched_data.retail_link)
    # if quiting:
    #     return likes_to_save
