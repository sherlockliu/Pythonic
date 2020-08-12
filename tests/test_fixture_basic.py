import pytest


@pytest.fixture(scope="function")
def before_1():
    print('\nbefore each test')


def test_1(before_1):
    print('test_1()')


def test_2(before_1):
    print('test_2()')
