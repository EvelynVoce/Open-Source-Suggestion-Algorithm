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
        
        self.list_of_lits_used_for_scores = {self.genres, self.directors, self.writers, self.cast, self.related_films}
        self.data_used_for_scores2: set[str] = {element for data in self.list_of_lits_used_for_scores for element in data.split(', ')}

    def get_data(self): #Gets the data for each film the user has liked
        for element in self.data_used_for_scores2:
            yield element
    
    def set_score(self, likes, already_watched):#Setting the score
        for like in likes:
            if like in self.data_used_for_scores2:
                self.score += 1
                
        if self.id in already_watched:
            self.score //=2
            #If the user has already watched that film make the score lower
            #This is so users dont get recommended the same films all the time

