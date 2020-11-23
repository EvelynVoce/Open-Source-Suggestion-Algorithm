from film_data_csv_reader import reading_csv
import binary_search
#############################   GIT VERSION

import cProfile, pstats, io

def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

#############################
# September 7th Jess moves out
#likes_to_update: list[int] = []
likes_to_update: list[int] = [x for x in range(500,600)]
likes_to_save: list[int] = [like_to_update for like_to_update in likes_to_update]
#A second list is made so films already used to calculate score do not need to be checked again 

#likes: list[int] = [0,2,3,4,5,6]

@profile
def suggestion_alorithm(list_of_film_data):
##    for like in likes_to_update:
##        for iterator in list_of_film_data[like].get_data():
##            data_of_index.append(iterator)
    
    data_of_index: list[str] = [iterator for like in likes_to_update for iterator in list_of_film_data[like].get_data()]
    #INSTEAD OF THIS TRY RETURNING THE DATA AS THE SET THAT IT IS BUT THEN COLLAPSING THIS ARRAY ON ITSELF SO ITS ONLY 1 DIMESNSIONAL
    likes_to_update.clear()
    #Compare each film with the data for the films the user likes
    for each_film in list_of_film_data:
        each_film.set_score(data_of_index)

    return list_of_film_data

def selecting_film(list_of_film_classes):
    like = input("\nWhat film do you like?").lower()
    #Binary Search
    list_of_film_classes.sort(key=lambda x: x.title) #Efficient sorting algorithm
    list_of_film_names = [film.title.lower() for film in list_of_film_classes]
    finding_film = binary_search.BinarySearch(list_of_film_names, like)
    if finding_film != None:
        likes_to_update.append(finding_film)
        max_likes(finding_film)
        
def max_likes(finding_film):
    if len(likes_to_save) >= 100:
        likes_to_save.pop(0)
    likes_to_save.append(finding_film)
    
def main():
    list_of_film_classes = reading_csv() # 0.1 seconds roughly
    while 1:
        list_of_film_classes = suggestion_alorithm(list_of_film_classes) #Uses the same variable as previously as to not use multiple variables for the same data
        list_of_film_classes.sort(key=lambda x: x.score, reverse=True) #Efficient sorting algorithm
        for x in range(10):
            print(list_of_film_classes[x].title + "\t" + str(list_of_film_classes[x].score)) #Faster to concatenate strings than to use ','
        selecting_film(list_of_film_classes)
main()






#USED TO ADD ID'S

##script_dir = os.path.dirname(__file__)  # Script directory
##script_dir, x = script_dir.rsplit('\\', 1)
##full_path = os.path.join(script_dir, 'films_data2.csv')
##with open(full_path, 'w', newline='') as file:
##    fieldnames = ['ID', 'title', 'release date', 'rating', 'genres', 'directors', 'writers', 'cast_names', 'related films']
##    writer = csv.DictWriter(file, fieldnames=fieldnames)
##    writer.writeheader()
##val = 0
##for film in list_of_film_classes:
##    with open(full_path, 'a', newline='') as file:
##        fieldnames = ['ID', 'title', 'release date', 'rating', 'genres', 'directors', 'writers', 'cast_names', 'related films']
##        writer = csv.DictWriter(file, fieldnames=fieldnames)
##        writer.writerow({'ID': val, 'title': film.title, 'release date': film.date, 'rating': film.rating, 'genres': film.genres, 'directors': film.directors,
##                         'writers': film.writers, 'cast_names': film.cast, 'related films': film.related_films})
##    val += 1


    
