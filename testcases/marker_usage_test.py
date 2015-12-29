__author__ = 'WLiu1'

import pytest
import sys
from time import sleep


@pytest.mark.integration # ~~~~~~~~~~~~~~~~ Marking whole classes or modules ~~~~~~~~~~~~~~~~~~~
class TestMarkerUsage(object):
    #~~~~~~~~~~~~~~~~~~~Manual Test ~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.fixture(scope="function", autouse=True)
    def validate_manual_tests(self, request):
        """
        Function to check if test is being run from a debugger.
        """
        if request.node.get_marker("manual") and not sys.gettrace():
            pytest.fail("~~~~~~ This test case must be run manually ~~~~~~")

    @pytest.mark.testcasename('MT100-005')
    @pytest.mark.manual
    def test_manual(self):
        """
        This test case should be run manually.
        """
        print "manual step1"
        sleep(5)
        print "manual step2"

    #~~~~~~~~~~~~~~~~~~~Smoke Test ~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.fixture(scope="function", autouse=True)
    def validate_smoke_tests(self, request):
        """
        Function to check if test is being run as a smoke test.
        """
        if request.node.get_marker("smoke") and not sys.gettrace():
            print "~~~~~~~~~ This test case is a smke test! ~~~~~~~~~"

    @pytest.mark.testcasename('MT200-005')
    @pytest.mark.smoke
    def test_smoke(self):
        """
        This test case should be run as smoke test.
        """
        print "smoke step1"
        sleep(5)
        print "smoke step2"