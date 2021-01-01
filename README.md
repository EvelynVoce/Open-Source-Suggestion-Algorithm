# Film-suggestion

This is an algorithm that will compare films the user likes against thousands of other films to accurately suggest films the user should like.
The data was scraped from IMDB using beautifulsoup. 

What I learned:
1) How to implement binary search using classes.
2) Sets vs lists for increasing performance.
3) List comprehensions
4) How to profile code so you can see what lines are taking the longest time to execute.


The film data includes:
Film title
Release date
Film genre
Directors
Writers
Cast
Related films


Account data includes:
Hashed usernames
Hashed Passwords


TV shows are included in this system too however they may be missing certain categories of data. In this case data may appear to be wrong in the csv file however the system still operates as intended despite this missing data. 
