import sys
import pprint

import src.app as app


def test_do_one():
    assert app.do_one == 1

def test_do_two():
    assert app.do_two == 2