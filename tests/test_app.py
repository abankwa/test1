import testconfigs
import sys
import pprint


import src.app as app

pprint.pprint(sys.path)

def test_do_one():
    assert app.do_one() == 1

def test_do_two():
    assert app.do_two() == 2

def test_do_three():
    assert True