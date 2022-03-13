import csv
import os
import Class_film_handling

script_dir = os.path.dirname(__file__)  # Script directory
script_dir, _ = script_dir.rsplit('\\', 1)  # Won't run correctly when running this file but will when running main
full_path = os.path.join(script_dir, 'films_data2.csv')
# full_path = os.path.join(script_dir, 'ExampleBooks.csv')


def reading_csv():
    with open(full_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')  # Read each line of the film_data.csv
        next(csv_reader)  # Skip the first line because it's just the headings for the columns
        list_of_film_data: list[object] = [Class_film_handling.FilmData(row) for row in csv_reader]
        # Creates a list of film class instances ^
        return list_of_film_data
