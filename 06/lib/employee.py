class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def display_info(self):
        print(f"Name, Surname: {self.name}, Job Title: {self.job_title}")
