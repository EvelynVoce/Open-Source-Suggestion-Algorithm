from film_data_csv_reader import reading_csv
import binary_search
import Accounts
import profiler  # This profiles the system so I can check if anything is too inefficient


# likes_to_update: list[int] = [0,2,3,4,5,6]
# Defining global variables at the module level.
likes_to_update: list[int] = []
likes_to_save: list[int] = []


@profiler.profile
def suggestion_algorithm(list_of_film_data):
    data_of_index: list[str] = [iterator for like in likes_to_update for iterator in list_of_film_data[like].get_data()]
    for like in likes_to_update:
        # Films watched checked here, not in selecting_film so films can be set to watched after program is closed
        if not list_of_film_data[like].watched:
            list_of_film_data[like].set_watched()

    # This is unnecessary on repeated runs^ there will only be one like so why bother sorting the films by id?/
    # Instead .get_data() on the list used for binary sort!

    likes_to_update.clear()
    for each_film in list_of_film_data:  # Compare each film with the data of the films the user likes
        each_film.set_score(data_of_index)
    return list_of_film_data


def selecting_film(list_of_film_classes):
    while True:  # Infinite loop uses return statement to break out
        like = input("\nWhat film do you like? (Enter Exit to quit)").lower()
        if like.lower() != "exit":
            # Binary Search
            list_of_film_classes.sort(key=lambda x: x.title)  # Sort by title so binary search can be performed
            finding_film = binary_search.binary_search(list_of_film_classes, like, len(list_of_film_classes) - 1)
            list_of_film_classes.sort(key=lambda x: x.id)  # Sort by ID so the films are ready to get the data
            if finding_film is not None:
                likes_to_update.append(finding_film)
                max_likes(finding_film, list_of_film_classes)
                return False
            else:
                print("That film was not found")
        else:
            return True
    

def max_likes(finding_film, list_of_film_classes):
    # The system only keeps track of the last 100 films the user likes between sessions
    if len(likes_to_save) >= 100:
        list_of_film_classes[likes_to_save[0]].set_not_watched()
        likes_to_save.pop(0)
    likes_to_save.append(finding_film)


def main():
    account = Accounts.main_menu()
    try:
        account_data = account[2].split(',')
    except IndexError:
        account_data = []

    global likes_to_update
    likes_to_update = [int(x) for x in account_data]

    # A second list is made so films already used to calculate score do not need to be checked again
    global likes_to_save
    likes_to_save = [like_to_update for like_to_update in likes_to_update]

    list_of_film_classes = reading_csv()  # 0.1 seconds roughly
    while 1:
        list_of_film_classes = suggestion_algorithm(list_of_film_classes)
        list_of_film_classes.sort(key=lambda x: x.score, reverse=True)  # Efficient sorting algorithm
        for x in range(10):
            print(list_of_film_classes[x].title + "\t" + str(
                list_of_film_classes[x].score))  # Faster to concatenate strings than to use ','

        quiting = selecting_film(list_of_film_classes)
        if quiting:
            Accounts.updating_account_data(account, likes_to_save)


main()
