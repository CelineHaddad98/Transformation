from models.deparment import Domain


def transform(data_in: dict) -> dict:
    emp_id = data_in['id']
    full_name = f"{data_in['first_name']} {data_in['last_name']}"

    department = data_in['department']
    domain = Domain[department].value

    adult = is_adult(data_in['age'])

    salary = data_in['salary']
    if(salary < 10000):
        tax_percent = 0
    elif(salary >= 10000 and salary < 20000):
        tax_percent = 10
    elif(salary >= 20000 and salary < 30000):
        tax_percent = 20
    elif(salary >= 30000 and salary < 40000):
        tax_percent = 30

    after_tax = salary - (salary * (tax_percent / 100))

    data_out = {}
    for variable in ["emp_id", "full_name", "adult", "domain","tax_percent", "after_tax"]:
        data_out[variable] = eval(variable)

    return data_out


def is_adult(age):
    return age > 18
