import pytest


def multiplicacao(x, y):

    return x * y


def test_mult():
    assert multiplicacao(10, 2) == 21


