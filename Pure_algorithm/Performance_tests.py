from example_main import example_main
from random import randint


def scalability_of_likes_test():
    # Change the length of likes to see how the data scales with respect to likes
    eg_likes: list[int] = [randint(1, 100) for _ in range(100)]  # Example user likes data
    eg_path: str = "films_data2.csv"
    example_main(eg_likes, eg_path)


def max_likes_test():
    # Test max number of likes if being enforced
    eg_likes: list[int] = [x for x in range(99)]  # Example user likes data
    eg_path: str = "films_data2.csv"
    example_main(eg_likes, eg_path)


# Performance test
if __name__ == "__main__":
    scalability_of_likes_test()
    # max_likes_test()
