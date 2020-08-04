"""
This is a stub to make cool data functions
"""
import pandas as pd


def print_test():
    """
    prints Hello World

    """
    print('hello world')


def to_data_frame(array: list) -> pd.DataFrame:
    """
    This function converts list to a DataFrame
    :param array: list
    :return: DataFrame
    """
    return pd.DataFrame(array)


if __name__ == '__main__':
    print_test()

    data = [5, 7, 8, 9, 10]
    to_data_frame(data)

    x = to_data_frame(data)

    print(type(x))



