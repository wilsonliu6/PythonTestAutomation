__author__ = 'WLiu1'

import pytest


class TestUtils(object):
    #~~~~~~~~~~~~~~~~~~~~~~~~setup and teardown functions~~~~~~~~~~~~~~~~~~~~~~
    @pytest.fixture(scope='function')
    def setup_function(self, request):
        def teardown_function():
            print "========================FUNCTION END %s ========================" % request.keywords.node.name

        request.addfinalizer(teardown_function)

        print "========================FUNCTION START %s ========================" % request.keywords.node.name

    @pytest.fixture(scope='module')
    def setup_module(self, request):
        def teardown_module():
            print "========================MODULE END %s ========================" % request.keywords.node.name

        request.addfinalizer(teardown_module)

        print "========================MODULE START %s ========================" % request.keywords.node.name

    #~~~~~~~~~~~~~~~~~~~~~~~setup and teardown function tests~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.mark.testcasename('FX100-005')
    def test_setup_function(self, setup_function):
        """
        Test fixture 'setup_function' which will be run each function.
        :param setup_function:
        :return:
        """
        print('test_setup_function called.')

    @pytest.mark.testcasename('FX200-005')
    def test_setup_module_1(self, setup_module):
        print('test_setup_module_1 called.')

    @pytest.mark.testcasename('FX200-010')
    def test_setup_module_2(self, setup_module):
        print('test_setup_module_2 called.')


    #~~~~~~~~~~~~~~~~~~~~~~~~function tests~~~~~~~~~~~~~~~~~~~~~~~~~
    @pytest.mark.testcasename('FT100-005')
    def test_func_1(self, my_utils):
        my_utils.func_1("test func1")

    @pytest.mark.testcasename('FT100-010')
    def test_func_2(self, my_utils):
        my_utils.func_2("test func2")

    @pytest.mark.testcasename('FT100-015')
    @pytest.mark.smoke_test
    @pytest.mark.parametrize(("a", "b"),
                             (
                             (1, 2),
                             (4,9),
                             )
                             )
    def test_add(self, my_utils, a, b):
        assert my_utils.add(a, b) == a+b


