class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_department_info(self):
        print(f"Department: {self.name}")
        print("Employees:")
        for employee in self.employees:
            employee.display_info()
