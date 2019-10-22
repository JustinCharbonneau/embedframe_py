from unittest import TestCase
from embedframe import utilities
import pandas as pd

use_data = pd.read_csv('embedframe/data/sample_text.csv')


def test_clean():
    s = utilities.clean_words(use_data)
    assert isinstance(s, pd.DataFrame)
