# asserting with assert statement

def func(x):
    return x+1
def test_answer():
    assert func(3)==5

# assertions about approximate equality
import numpy as np

def test_floats():
    assert (0.1 + 0.2) == pytest.approx(0.3)

def test_arrays():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.9999, 2.0001, 3.0])
    assert a == pytest.approx(b)