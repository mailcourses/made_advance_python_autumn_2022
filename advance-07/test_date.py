from unittest import mock
import pytest

from translator import is_ny, load_heavy_data


@pytest.fixture
def heavy_data():
    print("LOAD")
    return load_heavy_data("/var/models/data")


def test_predict_heavy(heavy_data):
    assert heavy_data["1"] == 1
    assert heavy_data["2"] == 2


def test_predict_heavy_update(heavy_data):
    assert heavy_data["1"] == 1
    assert heavy_data["2"] == 2


def test_predict_heavy_update_and_check(heavy_data):
    assert heavy_data["1"] == 1
    assert heavy_data["2"] == 2


@pytest.mark.parametrize(
    "month,day,expected",
    [
        (1, 0, "Not NY"),
        (2, 0, "Not NY"),
        (11, 0, "Not NY"),
        (0, 1, "Not NY"),
        (0, 31, "Not NY"),
        (1, 1, "Not NY"),
        (0, 0, "NY"),
    ],
)
def test_is_ny(month, day, expected):
    with mock.patch("translator.datetime") as mdate:
        mdate.now.return_value = mock.Mock(month=month, day=day)

        assert is_ny() == expected

