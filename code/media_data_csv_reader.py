import csv
import os
import Class_media_handling


def reading_csv(path: str):

    script_dir = os.path.dirname(__file__)  # Script directory
    script_dir, _ = script_dir.rsplit('\\', 1)  # Won't run correctly when running this file but will when running main
    full_path = os.path.join(script_dir, path)

    with open(full_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')  # Read each line of the given.csv
        next(csv_reader)  # Skip the first line because it's just the headings for the columns
        list_of_media_data: list[object] = [Class_media_handling.MediaData(row) for row in csv_reader]
        # Creates a list of media class instances ^
        return list_of_media_data
