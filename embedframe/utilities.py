from nltk.tokenize import TweetTokenizer
import gensim


def clean_words(column, remove_stopwords=False, column_header=False):
    """
    function that will clean a pandas text column
    :param column_header: boolean
    :param column: pandas text column
    :param remove_stopwords: boolean
    :return: tokenized array of text
    """

    tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

    all_words = []

    if column_header:
        for text in column[column_header]:
            tokenized_desc = tknzr.tokenize(text)
            all_words.append(tokenized_desc)
    else:
        for text in column:
            tokenized_desc = tknzr.tokenize(text)
            all_words.append(tokenized_desc)

    if remove_stopwords:
        # stopwords = ['the','is']
        print('removed_stopwords')

    return all_words


def generate_embedding(text_array, return_kv=True, size=100):

    assert gensim.models.word2vec.FAST_VERSION > -1, 'not fast version'

    word2vec_model = gensim.models.Word2Vec(text_array, size=size, window=5, min_count=10, workers=10, iter=5)

    if return_kv:
        return word2vec_model.wv
    else:
        return word2vec_model
