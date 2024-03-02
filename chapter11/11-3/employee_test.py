import pytest
from employee import Employee

@pytest.fixture
def employee():
    """An instance of Employee class available for all test cases"""
    employee = Employee('Chandra', 'Shekar', 160000)
    return employee

def test_give_default_raise(employee):
    """Test to check for a default raise."""
    new_annual_salary = employee.give_raise('')
    assert new_annual_salary == 165000

def test_give_custom_raise(employee):
    """Test to check for a custom raise."""
    new_annual_salary = employee.give_raise(8000)
    assert new_annual_salary == 168000