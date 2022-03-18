class MediaData:

    def __init__(self, data):  # Setting the values for class attributes
        self.id: int = int(data[0])
        self.title: str = data[1]
        self.date: str = data[2]

        # If developers need to access columns specifically by name they can name them as variables here
        # self.rating: str = data[3]
        self.genres: str = data[4]
        # self.directors: str = data[5]
        # self.writers: str = data[6]
        # self.cast: str = data[7]
        # self.related_films: str = data[8]

        self.score: int = 0
        self.viewed: bool = False
        list_of_lists_used_for_scores = {ele for ele in data[3:]}
        self.data_used_for_scores2: set[str] = {element for data in list_of_lists_used_for_scores for element in
                                                data.split(', ')}

    def get_data(self):  # Gets the data for each media the user has liked
        for element in self.data_used_for_scores2:
            yield element

    def set_viewed(self):
        self.viewed = True

    def set_not_viewed(self):
        # If is no longer in the list of likes_to_save then media is considered not seen
        self.viewed = False

    def set_score(self, likes):  # Setting the score
        unseen_media_score: int = 5
        seen_media_score: int = 1

        for like in likes:
            if like in self.data_used_for_scores2:
                if self.viewed:
                    self.score += seen_media_score
                else:
                    self.score += unseen_media_score  # Media score goes up 5 times slower

    # It's important to note that self.score += 0.2 is not the same as self.score /= 5 at the end.
    # Example:
    # Joker 16 with self.score += 0.5 would end up giving a score of 32
    # Joker 16 with self.score /= 2 at the end would give a score of 24
    # Joker goes up by 32 and is then halved as oppose to joker going up by half of 32 (16)
