from src.models.deparment import Domain


def transform(data_in: dict) -> dict:
    data_out = {
        "emp_id": data_in['id'],
        "full_name": f"{data_in['first_name']} {data_in['last_name']}",
        "domain": Domain[data_in['department']].value
    }

    data_out["adult"] = is_adult(data_in['age'])

    tax_percent = get_tax_percent(data_in['salary'])
    data_out["tax_percent"] = tax_percent

    data_out["after_tax"] = calculate_salary_after_tax(data_in['salary'], tax_percent)

    return data_out


def is_adult(age):
    return age > 18


def get_tax_percent(salary: int) -> float:
    if(salary < 10000):
        return 0
    elif(salary >= 10000 and salary < 20000):
        return 10
    elif(salary >= 20000 and salary < 30000):
        return 20
    elif(salary >= 30000 and salary < 40000):
        return 30


def calculate_salary_after_tax(salary: int, tax_percent: float) -> float:
    return salary - (salary * (tax_percent / 100))
