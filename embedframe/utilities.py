# import pandas as pd


def clean_words(column, remove_stopwords=False, column_header=False):
    """
    function that will clean a pandas text column
    :param column_header: boolean
    :param column: pandas text column
    :param remove_stopwords: boolean
    :return: tokenized array of text
    """
    if remove_stopwords:
        # stopwords = ['the','is']
        print('removed_stopwords')

    if column_header:
        print('Theres a header!')

    return column.head(2)

