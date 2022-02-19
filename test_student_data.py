from student_data import StudentDB
import pytest

"""Running tests using python fixtures 
    the module parameter tells python that the fixture is a module wise function therefore the print setup statement should be 
    printed only once.
"""
@pytest.fixture(scope="module")
def db():
    print("-------------Setup-------------")
    db = StudentDB()
    db.connect("student_data.json")
    yield db
    print("-------------Teardown----------")
    db.close()

def test_scott_data(db):
    scott_data = db.get_data("Scott")
    assert scott_data["id"] == 1
    assert scott_data["name"] == "Scott"
    assert scott_data["result"] == "pass"
    
    
def test_mark_data(db):
    mark_data = db.get_data("Mark")
    assert mark_data["id"] == 1
    assert mark_data["name"] == "Mark"
    assert mark_data["result"] == "fail"