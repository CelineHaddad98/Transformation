import json
import enum


class Domain(enum.Enum):
    IT =  "it-services.com" 
    SALES = "sales-dep.com"
    PRESALES = "pre-sales.com"
    FULFILLMENT = "fulfillment.com"
    SUPPORT = "customer-support.com"


def transform(data_in: dict) -> dict:
    emp_id = data_in['id']
    full_name = data_in['first_name'] + " " + data_in['last_name']
    adult = True if data_in['age']>18 else False
    department = data_in['department']
    domain = Domain[department].value
    salary = data_in['salary']
    if(salary < 10000):
        tax_percent = 0
    elif(salary>=10000 and salary<20000):
        tax_percent = 10
    elif(salary>=20000 and salary<30000):
        tax_percent = 20
    elif(salary>=30000 and salary<40000):
        tax_percent = 30


    after_tax = salary - (int)(salary * (tax_percent/100))

    data_out={}
    for variable in ["emp_id", "full_name", "adult", "domain","tax_percent", "after_tax"]:
        data_out[variable] = eval(variable)

   
    return data_out



file = open('input.json')
lines = file.readlines()
file.close()


outfile = open("output.json" ,"w")

for line in lines:
    edited = transform(json.loads(line))
    outfile.write(json.dumps(edited, indent = 4))


outfile.close()








