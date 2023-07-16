import pytest

def add_three(n):
    return n + 3

def add(n):
    return n+n

# Markers are used to separate func test into different categories and being able to run separetly
# NOTE: Requires a <marker_name> addition in pytest.ini file

@pytest.mark.add
def test_add_three():
    assert add_three(2) == 5
    
    
def test_add():
    assert add(2) == 4
    assert add(1) == 2
    assert add(0) == 0
    
# Fixtures to supply data required for the function test, variables, linkes, connections and etc.
@pytest.fixture
def input_value():
    input = 39
    return input

def test_divis_by_3(input_value):
    assert input_value % 3 == 0
    
