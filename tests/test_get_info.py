import pytest
import sys, os

# Since the tests can be executed on different OS, let's specify path explicitly:
p = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
sys.path.append(p)

from data import get_info
from pandas import read_pickle

def test_correct_compound_passed_to_get_info():
    """
    Happy path for getting and comparing not empty parameters from the Series.
    """
    _ = os.path.join(os.path.dirname(__file__), "18W.pkl")
    expected = read_pickle(_)
    content = expected.dropna() == get_info("18W").dropna()
    assert content.all()

def test_no_compound_passed_to_get_info():
    """
    Verify default compound trigger when no parameter passed.
    """
    _ = os.path.join(os.path.dirname(__file__), "ADP.pkl")
    expected = read_pickle(_)
    assert get_info()["name"] == expected["name"]

def test_incorrect_compound_passed_to_get_info():
    """
    Verify that function will return error as expected
    """
    with pytest.raises(KeyError):
        get_info("N0N3")
