# REQUESTING FIXTURES

import pytest

class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True

class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)
    assert all(fruit.cubed for fruit in fruit_salad.fruit)

# FIXTURE REQUESTING ANOTHER FIXTURE

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return [first_entry]

def test_string(order):
    order.append("b")
    assert order == ["a", "b"]

# REUSING FIXTURE

def test_int(order):
    order.append(3)
    assert order == ["a", 2]

# ONE FIXTURE CALLING MULTIPLE FIXTURES AT A TIME

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def second_entry():
    return 2

@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]

def test_string1(order, expected_list):
    order.append(3.0)
    assert order == expected_list
# CALLING ONE FIXTURE MULTIPLE TIMES

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order():
    return []

@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)

def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]
# AUTO USE FIXTURES

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return []

@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)

def test_string_only(order, first_entry):
    assert order == [first_entry]

def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]