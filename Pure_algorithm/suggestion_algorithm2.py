import binary_search
from SearchClass import SearchData
from media_data_csv_reader import reading_csv


def suggestion_algorithm_single_use(likes_to_save: list[int], given_path: str):
    # Defining global variables at the module level.
    list_of_media_classes = reading_csv(given_path)

    # This includes features that only need to be run at the start like setting saved media to seen
    data_of_index: list[str] = [data for like in likes_to_save for data in list_of_media_classes[like].get_data()]
    for like in likes_to_save:
        # Media seen checked here, not in selecting_media so media can be set to seen after program is closed
        if not list_of_media_classes[like].viewed:
            list_of_media_classes[like].set_viewed()

    return list_of_media_classes, data_of_index


def suggestion_algorithm(list_of_media_classes, media_data_to_set_scores):
    for each_item in list_of_media_classes:  # Compare each item with the data of the media the user likes
        each_item.set_score(media_data_to_set_scores)


def directing_to_retailer(title: str) -> str:
    amazon_link: str = "https://www.amazon.com/s?k="
    full_link: str = amazon_link + title.replace(" ", "+")
    return full_link


def selecting_media(likes_to_save, like, list_of_media_classes):
    list_of_media_classes.sort(key=lambda x: x.title)  # Sort by title so binary search can be performed
    found_item = binary_search.binary_search(list_of_media_classes, like.lower(), len(list_of_media_classes) - 1)
    if found_item is not None:
        # data_of_index can be a set here because duplicates aren't relevant when only one media is considered
        data_of_index: set = {iterator for iterator in list_of_media_classes[found_item].get_data()}
        list_of_media_classes[found_item].set_viewed()
        found_item_id: int = list_of_media_classes[found_item].id
        likes_to_save = max_likes(found_item_id, likes_to_save, list_of_media_classes)

        amazon_link = directing_to_retailer(like)
        searched_data = SearchData(data_of_index, amazon_link)
        return searched_data, likes_to_save


def max_likes(found_item_id, likes_to_save, list_of_media_classes):
    # The system only keeps track of the last 100 items the user likes between sessions
    if len(likes_to_save) >= 100:
        list_of_media_classes.sort(key=lambda x: x.id)  # Needed to set the items to not viewed
        list_of_media_classes[likes_to_save[0]].set_not_viewed()
        likes_to_save.pop(0)
    likes_to_save.append(found_item_id)
    return likes_to_save


def output_relevant_items(list_of_media_classes):
    list_of_media_classes.sort(key=lambda x: x.score, reverse=True)  # Sorting items by score
    for item in list_of_media_classes[:10]:  # Print items in order of predicted preference
        print(item.title, item.score)


# Below is a basic example of how to integrate the algorithm into existing software.
# Change eg_user_likes with a list of ID's for items the user likes.
# Change eg_path with a path to the csv with all items

def example_main(users_likes: list[int], dataset_path: str):
    list_of_media_classes, liked_data = suggestion_algorithm_single_use(users_likes, dataset_path)  # Get data from liked items
    while True:
        suggestion_algorithm(list_of_media_classes, liked_data)  # Set item scores based on liked data
        output_relevant_items(list_of_media_classes)

        selected_film = input("name a film")
        try:  # Get data for item except when item not found
            data_and_link, id_to_save = selecting_media(users_likes, selected_film, list_of_media_classes)
            # id_to_save can be added to user data and stored in the database to save user interests between sessions
            liked_data = data_and_link.data
            print(data_and_link.retail_link)  # link to purchase selected item
        except TypeError:
            pass


if __name__ == "__main__":
    eg_user_likes: list[int] = []  # Example user likes data
    path: str = "films_data2.csv"
    example_main(eg_user_likes, path)
