from marula import __version__
from marula.marula import Marula


def test_version():
    assert __version__ == '0.1.0'


def test_add():
    fruit = Marula()
    assert fruit.run([10, 10, "op_add"]) == 20

    
def test_zerodiv():
    fruit = Marula()
    assert fruit.run([33, 0, "op_div"]) == 33


def test_sign():
    fruit = Marula()
    assert fruit.run([-11, "op_sign"]) == -1

    
def test_negative():
    fruit = Marula()
    assert fruit.run([-71, "op_neg"]) == 71
    
def test_argmax():
    fruit = Marula()
    assert fruit.run([17, 8, "op_argmax"]) == 17

    
def test_tanh():
    fruit = Marula()
    assert fruit.run([5.7, "op_tanh"]) == 0.999978
