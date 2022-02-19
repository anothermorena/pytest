import math_func #it imports the math func python script in the same directory as the test file
import pytest

    
#define test functions

@pytest.mark.skip(reason="Just demo of this decorator") 
def test_add():
    assert math_func.add(7,3) == 10 #checks whether the function returns 10 or not. This is called assertion
    assert math_func.add(7) == 9
    assert math_func.add(8) == 10
    assert math_func.add(4) == 6
    
@pytest.mark.number  #assigns a maker called number to this function 
def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14 
    
@pytest.mark.string #assigns a maker called string to this functon    
def test_add_strings():
    result = math_func.add("Hello ","World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Heldlo" not in result

@pytest.mark.string    
def test_product_string():
    assert math_func.product("Hello ", 3) == "Hello Hello Hello "
    result = math_func.product("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result
    
    
#Using Pytest's parameterize decorator 
#p in the function below stands for parameterize
    """
            1)x and y are user defined variable. They can be named or called anything
            2)the result argumrnt is what you want to assert,
            3)you pass the things you want to test as an iterable i.e array of tuples as seen below
            
    """
@pytest.mark.parametrize("x,y,result",[
    (7,3,10),
    ("Hello ","World","Hello World"),
    (10.5,25.5, 36)
])
def test_add_p(x,y,result): #you pass the same parameter names you declared above to the function
    assert math_func.add(x,y) == result
    