__author__ = 'WLiu1'

import pytest

from lib.Utils import Utils
from lib.MyConfigParser import MyConfigParser

@pytest.fixture(scope='class', autouse=False)
def my_utils():
    return Utils()

@pytest.fixture(scope='session', autouse=True)
def my_config():
    return MyConfigParser()