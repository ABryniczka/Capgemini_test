class Field:
    def __init__(self):
        self.employers = []
        self.departments = []

    class Employer:
        def __init__(self, first_name: str, last_name: str, age: int, job: str, salary: int, bonus: int):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.job = job
            self.salary = salary
            self.bonus = bonus
            self.total_salary = self.salary

        def apply_bonus(self):
            self.total_salary = self.salary + self.bonus

    class Department:
        def __init__(self, name: str):
            self.name = name
            self.users = []

        def add_employer_to_department(self, new_employer):
            self.users.append(new_employer)
            return f'New user has been added'

        def display_employers(self):
            lists = [user.first_name for user in self.users]
            return lists

        def remove_employer_from_department(self, employee):
            self.users.remove(employee)
            return f'Last Employee from department {self.name} list has been removed'

    def add_employer(self, first_name: str, last_name: str, age: int, job: str, salary: int, bonus: int):
        self.employers.append(Field.Employer(first_name, last_name, age, job, salary, bonus))

    def remove_employer(self):
        self.employers.pop()
        return f'Last Employee from Field company list has been removed'

    def add_department(self, name: str):
        self.departments.append(Field.Department(name))

    def remove_department(self):
        self.departments.pop()
        return f'Last Department from Field company list has been removed'

    def display_departments(self):
        lists = [dep.name for dep in self.departments]
        return lists


if __name__ == "__main__":
    company = Field()
    # -------------------
    user = company.Employer('Jan', 'Kowalski', 25, 'Student', 0, 1000)
    print(user.first_name)
    # -------------------
    company.add_employer('Janusz', 'Nowak', 25, 'Architect', 2100, 1000)
    company.add_employer('Mateusz', 'Gał', 26, 'Mechanic', 2500, 1200)
    # -------------------
    company.add_department('DevOps')
    company.add_department('Backend')
    company.add_department('Frontend')
    # -------------------
    print(company.employers[0].total_salary)
    company.employers[0].apply_bonus()
    print(company.employers[0].total_salary)
    # -------------------
    print(company.departments[0].add_employer_to_department(company.employers[0]))
    print(company.departments[0].add_employer_to_department(company.employers[1]))
    company.departments[0].add_employer_to_department(user)
    print(company.departments[0].users[0].first_name)
    # -------------------
    print(company.display_departments())
    print(company.remove_department())
    print(company.display_departments())
    # -------------------
    print(company.departments[0].display_employers())
    print(company.departments[0].remove_employer_from_department(user))
    print(company.departments[0].display_employers())
    # -------------------
