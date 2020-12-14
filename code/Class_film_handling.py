class Film_data:
    
    def __init__(self, data): #Setting the values for class attributes
        self.id = int(data[0])
        self.title = data[1]
        self.date = data[2]
        self.rating = data[3]
        self.genres = data[4]
        self.directors = data[5]
        self.writers = data[6]
        self.cast = data[7]
        self.related_films = data[8]
        self.score = 0
        self.watched = False
        list_of_lits_used_for_scores = {self.genres, self.directors, self.writers, self.cast, self.related_films}
        self.data_used_for_scores2: set[str] = {element for data in list_of_lits_used_for_scores for element in data.split(', ')}


    def get_data(self): #Gets the data for each film the user has liked
        for element in self.data_used_for_scores2:
            yield element

            
    def set_watched(self):
        self.watched = True

    
    def set_not_watched(self):
        # If is no longer in the list of likes_to_save then film is considered not watched
        self.watched = False
                

    def set_score(self, likes):#Setting the score
        for like in likes:
            if like in self.data_used_for_scores2:
                if self.watched:
                    self.score += 0.2
                
                else:
                    self.score += 1 # Film score goes up 5 times slower


    # It's important to note that self.score += 0.2 is not the same as self.score /= 5 at the end.
    # Example:
    # Joker 16 with self.score += 0.5 would end up giving a score of 32
    # Joker 16 with self.score /= 2 at the end would give a score of 24
    # Joker goes up by 32 and is then halved as oppose to joker going up by half of 32 (16)
