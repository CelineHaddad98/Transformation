from unittest import result
from src.transformers.employee_transformer import is_adult, get_tax_percent, calculate_salary_after_tax, transform


def test_is_adult():
    assert is_adult(15) == False
    assert is_adult(20) == True
    assert is_adult(18) == False


def test_get_tax_percent():
    assert get_tax_percent(900) == 0
    assert get_tax_percent(9999) == 0
    assert get_tax_percent(10000) == 10
    assert get_tax_percent(10001) == 10
    assert get_tax_percent(19999) == 10
    assert get_tax_percent(20000) == 20
    assert get_tax_percent(29999) == 20
    assert get_tax_percent(30000) == 30
    assert get_tax_percent(39999) == 30


def test_calculate_salary_after_tax():
    assert calculate_salary_after_tax(25000, 20) == 20000
    assert calculate_salary_after_tax(500, 0) == 500
    assert calculate_salary_after_tax(10000, 10) == 9000
    assert calculate_salary_after_tax(30000, 30) == 21000


def test_transform():
    test_data = {
        "id": "123",
        "first_name": "Belal",
        "last_name": "Ali",
        "age": 15,
        "department": "IT",
        "salary": 35000
    }

    result = transform(test_data)

    expected_data = {
        "emp_id": "123",
        "full_name": "Belal Ali",
        "adult": False,
        "domain": "it-services.com",
        "tax_percent": 30,
        "after_tax": 24500
    }
    assert result == expected_data

    test_data = {
        "id": "456",
        "first_name": "Ameer",
        "last_name": "Adhami",
        "age": 26,
        "department": "SALES",
        "salary": 6500
    }

    result = transform(test_data)

    expected_data = {
        "emp_id": "456",
        "full_name": "Ameer Adhami",
        "adult": True,
        "domain": "sales-dep.com",
        "tax_percent": 0,
        "after_tax": 6500
    }

    assert result == expected_data

