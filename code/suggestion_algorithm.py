from film_data_csv_reader import reading_csv
import binary_search
import profiler  # This profiles the system, so I can check if anything is too inefficient
from os import system

# Defining global variables at the module level.
list_of_film_classes = []


# @profiler.profile
def suggestion_algorithm_single_use(likes_to_save: list[int]):
    # This includes features that only need to be run at the start like setting saved films to watched
    data_of_index: list[str] = [data for like in likes_to_save for data in list_of_film_classes[like].get_data()]
    for like in likes_to_save:
        # Films watched checked here, not in selecting_film so films can be set to watched after program is closed
        if not list_of_film_classes[like].watched:
            list_of_film_classes[like].set_watched()

    return data_of_index


@profiler.profile
def suggestion_algorithm(film_data_to_set_scores):
    for each_film in list_of_film_classes:  # Compare each film with the data of the films the user likes
        each_film.set_score(film_data_to_set_scores)


def directing_to_retailer(name: str):
    pass


def selecting_film(likes_to_save):
    user_wants_to_exit = True

    while True:  # Infinite loop uses return statement to break out
        like = input("\nWhat film do you like? (Enter Exit to quit)").lower()
        system('cls')
        if like == "exit":
            print("exit engaged")
            return user_wants_to_exit, None

        # Binary Search
        list_of_film_classes.sort(key=lambda x: x.title)  # Sort by title so binary search can be performed
        finding_film = binary_search.binary_search(list_of_film_classes, like, len(list_of_film_classes) - 1)
        if finding_film is not None:
            # data_of_index can be a set here because duplicates aren't relevant when only one film is considered
            data_of_index: set = {iterator for iterator in list_of_film_classes[finding_film].get_data()}
            list_of_film_classes[finding_film].set_watched()
            found_film_id: int = list_of_film_classes[finding_film].id
            max_likes(found_film_id, likes_to_save)
            return (not user_wants_to_exit), data_of_index
        else:
            input("That film was not found - press any key to continue")
            system('cls')
    

def max_likes(found_film_id, likes_to_save):
    # The system only keeps track of the last 100 films the user likes between sessions
    if len(likes_to_save) >= 100:
        list_of_film_classes.sort(key=lambda x: x.id)  # Needed to set the film to not watched
        list_of_film_classes[likes_to_save[0]].set_not_watched()
        likes_to_save.pop(0)
    likes_to_save.append(found_film_id)


def main_algorithm(account_data):
    # A second list is made so films already used to calculate score do not need to be checked again
    likes_to_save: list[int] = [int(x) for x in account_data]

    global list_of_film_classes
    list_of_film_classes = reading_csv()  # 0.1 seconds roughly
    film_data_to_set_scores = suggestion_algorithm_single_use(likes_to_save)
    system('cls')  # Clears the screen

    while 1:
        suggestion_algorithm(film_data_to_set_scores)
        list_of_film_classes.sort(key=lambda x: x.score, reverse=True)  # Efficient sorting algorithm
        for x in range(len(list_of_film_classes)):
            print(list_of_film_classes[x].title + "\t" + str(
                list_of_film_classes[x].score))  # Faster to concatenate strings than to use ','

        quiting, film_data_to_set_scores = selecting_film(likes_to_save)
        if quiting:
            return likes_to_save
