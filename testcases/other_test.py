__author__ = 'WLiu1'

import pytest

######################## Asserting with the assert statement ###################
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

#################### Asserting that a certain exception is raised ####################
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

####################  Raising a specific test outcome (fail, skip) ####################
def test_pytest_skip():
    pytest.skip("Skip this test")

def test_pytest_fail():
    pytest.fail("Pytest Fail")