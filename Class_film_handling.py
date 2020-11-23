import numpy as np
class Film_data:
    
    def __init__(self, data): #Setting the values for class attributes
        self.id = data[0]
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
    
    def set_score(self, likes):#Setting the score (MUST BE DONE IN A SEPERATE CLASS METHOD BECAUSE IT NEEDS TO BE RECALLED)
        for like in likes:
            if like in self.data_used_for_scores2:
                self.score += 1




##    def setting_score(self, likes):
##        #Setting the score (MUST BE DONE IN A SEPERATE CLASS METHOD WHEN IT NEEDS TO BE RECALLED)
##        list_of_attritbutes = [self.genres, self.directors,self.writers, self.cast, self.related_films]
##        comparable_data_attr = set([element for attribute in list_of_attritbutes for element in attribute.split(', ')])
##        self.score = len(comparable_data_attr.intersection(likes))





##    def set_score(self, likes):#Setting the score (MUST BE DONE IN A SEPERATE CLASS METHOD BECAUSE IT NEEDS TO BE RECALLED)
##        list_of_attritbutes = [self.genres, self.directors,self.writers, self.cast, self.related_films]
##        comparable_data_attr = [element for attribute in list_of_attritbutes for element in attribute.split(', ')]
##        comparable_data = [like for like in likes if like in comparable_data_attr] #IF DATA IN LIKES TAKES UP OVER 2 SECONDS OF COMPLEXITY
##
##        import time
##        print(likes + '\n')
##        print(comparable_data_attr)
##        time.sleep(1000)
##        self.score = len(comparable_data)




####  VERY SLOW #########################
##    def set_score(self, likes):#Setting the score (MUST BE DONE IN A SEPERATE CLASS METHOD BECAUSE IT NEEDS TO BE RECALLED)
##        self.score = SequenceMatcher(None, self.data_used_for_scores, likes).ratio()


# IDEA FIND THE COSINE SIMILARITY BETWEEN LIKES AND LIST OF ATTRIBUTES AND SET THE SCORE AS A VALUE BETWEEN 0 AND 1. THIS SHOULD REMOVE THE TIME COMPLEXITY OF THE LIST COMPREHENSIONS






##    def setting_score(self, likes):
##        #Setting the score (MUST BE DONE IN A SEPERATE CLASS METHOD WHEN IT NEEDS TO BE RECALLED)
##        list_of_attritbutes = [self.genres, self.directors,self.writers, self.cast, self.related_films]
##        comparable_data_attr = set([element for attribute in list_of_attritbutes for element in attribute.split(', ')])
##        self.score = len(comparable_data_attr.intersection(likes))
        
        #Maybe by sorting the list of likes first you could break out of a searching loop when the system realises the item its searching for isn't present 


    
##        import time
##        print(len(likes))
##        print(len(comparable_data))
##        time.sleep(10)
        
##        #Setting the score
##        likes = set(likes) #SET REMOVES DUPLICATE DATA MEANING SCORE IS WRONG! USING SETS MASSIVELY IMPROVES TIME COMPLEXITY
##        list_of_attritbutes = [self.genres, self.directors, self.writers, self.cast, self.related_films]
##        comparable_data = [element for attribute in list_of_attritbutes for element in attribute.split(', ') if element in likes]
##        #union_list = likes.intersection(comparable_data)
##        self.score = len(comparable_data)


##class Film_data:
##    
##    def __init__(self, data, likes):
##
##        self.title, self.date, self.rating, self.genres, self.directors, self.writers, self.cast, self.related_films = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]
##        
##        #Setting the score
##        list_of_attritbutes = [self.genres, self.directors, self.writers, self.cast, self.related_films]
##        comparable_data_attr = [element for attribute in list_of_attritbutes for element in attribute.split(', ')]
##        comparable_data = [like for like in likes if like in comparable_data_attr]
##        self.score = len(comparable_data)



##class Film_data:
##    
##    def __init__(self, data):
##        self.title = data[0]
##        self.date = data[1]
##        self.rating = data[2]
##        self.genres = data[3]
##        self.directors = data[4]
##        self.writers = data[5]
##        self.cast = data[6]
##        self.related_films = data[7]
##        self.score = 0
##
##
##    def set_score(self, likes, data): #data isn't important passed in to allow other version to run
##        list_of_attritbutes = [self.genres, self.directors, self.writers, self.cast, self.related_films]
##        for attribute in list_of_attritbutes:
##            union_list = self.intersection(attribute.split(', '), likes)
##            self.score += len(union_list)
##
##    def set_score(self, likes, data):
##        union_list = self.intersection(str(data).replace("'", "").split(', '), likes)
##        self.score += len(union_list)
##        
##    def intersection(self, lst1, lst2):
##        return set(lst1).intersection(lst2)

        








#### THIS FIXES A VERY UNLIKELY PROBLEM AS LISTED BELOW:

## THIS PROBLEM COULD HOWEVER BE A POSITIVE THING. IE IF IS RELATED TO SPIDER-MAN 2 AND THE USER LIKES SPIDER-MAN, THE QUICKER METHOD ACTUALLY ATTRIBUTES AN EXTRA POINT TO SPIDER-MAN 2

##                # ALTERNATE CODE SLOWER BY 0.4 SECONDS BUT REMOVES THE ERROR
##                attribute = attribute.replace(', ', ',')
##                attribute_list = attribute.split(',')    # (', ')                
##                for attribute_string in attribute_list:
##                    if like == attribute_string.strip():
##                        self.score += 1
                
# The third loop could be eliminated by using if like in attrubte_list instead but would have an unlikely but major error
# If the like was Frank Oz but the attribute was Frank Oze the score would still go up even though it shoudn't because Frank Oz is in Frank Oze
# However Frank Oz != Frank Oze so this solution is prefered 



