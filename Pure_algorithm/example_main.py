# Below is a basic example of how to integrate the algorithm into existing software.
# Change eg_user_likes with a list of ID's for items the user likes.
# Change eg_path with a path to the csv with all items

from suggestion_algorithm2 import suggestion_algorithm_single_use, suggestion_algorithm, get_items, selecting_media


def output_items(list_of_media_classes, liked_data):
    suggestion_algorithm(list_of_media_classes, liked_data)  # Set item scores based on liked data
    list_of_items = get_items(list_of_media_classes)

    number_of_items_output: int = 5
    for item in list_of_items[:number_of_items_output]:
        print(item.title, item.score)


def example_main(users_likes: list[int], path: str):
    list_of_media_classes, liked_data = suggestion_algorithm_single_use(users_likes, path)
    output_items(list_of_media_classes, liked_data)
    while True:
        selected_film = input("name a film")
        try:  # Get data for item except when item not found
            data_and_link, id_to_save = selecting_media(users_likes, selected_film, list_of_media_classes)
            # id_to_save can be added to user data and stored in the database to save user interests between sessions
            liked_data = data_and_link.data
            print("\n", data_and_link.retail_link)  # link to purchase selected item
            output_items(list_of_media_classes, liked_data)
        except TypeError:
            print("Error")


# if __name__ == "__main__":
#     eg_likes: list[int] = []  # Example user likes data
#     eg_path: str = "films_data2.csv"
#     example_main(eg_likes, eg_path)


# Performance test
if __name__ == "__main__":
    from random import randint
    eg_likes: list[int] = []  # Example user likes data
    print(len(eg_likes))
    eg_path: str = "films_data2.csv"
    example_main(eg_likes, eg_path)

    # from matplotlib import pyplot as plt
    # num_items = [10, 25, 50, 100, 250, 500, 1000]
    # run_time = [0.030, 0.082, 0.162, 0.313, 0.775, 1.560, 3.129]
    #
    # plt.title("A graph to show how run time scales in relation to the number of known user interests")
    # plt.xlabel("Number of users saved interests")
    # plt.ylabel("Run-time (seconds)")
    #
    # plt.plot(num_items, run_time, color='red', marker='o')
    # plt.savefig('alg2-runtime.png', bbox_inches="tight")


    # from matplotlib import pyplot as plt
    # num_items = [10, 25, 50, 100, 250, 500, 1000]
    # run_time = [0.004 for x in range(len(num_items))]
    #
    # plt.title("A graph to show how run time scales in relation to the number"
    #           " of known user interests when a new item is selected")
    # plt.xlabel("Number of users saved interests")
    # plt.ylabel("Run-time (seconds)")
    #
    # plt.plot(num_items, run_time, color='red', marker='o')
    # plt.savefig('alg2-runtime_average_case.png', bbox_inches="tight")

    from matplotlib import pyplot as plt
    num_items = [250, 500, 1000, 1500, 2000, 2500]
    run_time = [0.032, 0.058, 0.120, 0.174, 0.219, 0.276]

    plt.title("A graph to show how run time scales in relation to the size of the dataset")
    plt.xlabel("Number of items in the dataset")
    plt.ylabel("Run-time (seconds)")

    plt.plot(num_items, run_time, color='red', marker='o')
    plt.savefig('alg2-runtime_data_scale.png', bbox_inches="tight")
