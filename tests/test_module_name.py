import pytest
import requests_mock

from src.package_name.module_name import google_up, add


@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        yield m


def test_google_up(mock_api):
    mock_api.get("https://google.com/", text='ok', status_code=200)
    assert google_up() is True

    mock_api.get("https://google.com/", text='fail', status_code=400)
    assert google_up() is False


def test_add_positive_numbers():
    assert add(1, 2) == 3
