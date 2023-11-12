from lib.employee import Employee
from lib.department import Department


employee1 = Employee("Janis Berzins", "Software Engineer")
employee2 = Employee("Anna Berzina", "Security Consultant")

it_department = Department("IT Department")

it_department.add_employee(employee1)
it_department.add_employee(employee2)

it_department.display_department_info()
