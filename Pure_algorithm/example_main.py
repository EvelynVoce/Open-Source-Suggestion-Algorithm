# Below is a basic example of how to integrate the algorithm into existing software.
# Change eg_user_likes with a list of ID's for items the user likes.
# Change eg_path with a path to the csv with all items

from suggestion_algorithm2 import suggestion_algorithm_single_use, suggestion_algorithm, get_items,\
                                  selecting_media


def output_items(list_of_media_classes, liked_data):
    suggestion_algorithm(list_of_media_classes, liked_data)  # Set item scores based on liked data
    list_of_items = get_items(list_of_media_classes)

    number_of_items_output: int = 5
    for item in list_of_items[:number_of_items_output]:
        print(item.title, item.score)


def example_main(users_likes, path):
    list_of_media_classes, liked_data = suggestion_algorithm_single_use(users_likes, path)
    output_items(list_of_media_classes, liked_data)

    selected_film = input("name a film")
    try:  # Get data for item except when item not found
        data_and_link, id_to_save = selecting_media(users_likes, selected_film, list_of_media_classes)
        # id_to_save can be added to user data and stored in the database to save user interests between sessions
        liked_data = data_and_link.data
        print("\n", data_and_link.retail_link)  # link to purchase selected item
        output_items(list_of_media_classes, liked_data)
    except TypeError:
        print("Error")


if __name__ == "__main__":
    eg_likes: list[int] = []  # Example user likes data
    eg_path: str = "films_data2.csv"

    example_main(eg_likes, eg_path)
