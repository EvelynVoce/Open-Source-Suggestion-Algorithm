# Open-Source Suggestion Algorithm

This is an open source suggestion algorithm (also known as a recommender system) that uses content-based filtering to suggest content to users. An example dataset along with a demo application are present that uses film data to suggest media to users. This data was scraped from IMDB using beautifulsoup. However it is important to note this algorithm has been created from the ground up with user customisation in mind, this algorithm can be used in a range of settings such as e-commerce sites so that companies can target products to their users.

If you wish to utilise this algorithm in your own application you are free to do so. Please note however that datasets must be given as csv files and their first ID's must be stored sequentially. This is so that when sorted, an items ID will correspond to an items index, allowing for random access and thus constant time complexity. 

What I learned:
1) How to implement binary search using classes.
2) Sets vs lists for increasing performance.
3) List comprehensions
4) How to profile code so you can see what lines are taking the longest time to execute.


The film data includes:
Film title,
Release date,
Film genre,
Directors,
Writers,
Cast and
Related films


Account data includes:
Hashed usernames,
Hashed Passwords and
watched films
