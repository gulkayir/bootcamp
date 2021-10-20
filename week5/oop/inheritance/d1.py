#EMPLOYEE

class Employee:

    stuff = []


    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.id = self.generate_id()
        Employee.stuff.append({
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name

        })


    def __str__(self):
        return f'{self.name} {self.last_name}'

    def generate_id(self):
        import random
        id_ = random.randint(500,506)
        for worker in Employee.stuff:
            if worker.get('id') == id_:
                return self.generate_id()
        return id_


class SalaryEmployee(Employee):
    def __init__(self, name, last_name, salary):
        super().__init__(name, last_name)
        info = {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name
        }
        self.salary = salary
        for worker in Employee.stuff:
            if info == worker:
                worker.update({'salary': self.salary})
        

class HourlyEmployee(Employee):
    def __init__(self, name, last_name, hours, per_hour):
        super().__init__(name, last_name)
        info1 = {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name
        }
        self.salary = hours * per_hour
        for worker in Employee.stuff:
            if info1 == worker:
                worker.update({'salary': self.salary})
        


harry = Employee('Harry', 'Potter')
hermione = Employee('Hermione', 'Granger')
ron = Employee('Ron','Weasley')
draco = SalaryEmployee('Draco','Malfoy',7259234)
blaze = HourlyEmployee('Blaze', 'Zabiny',100,25)
print(Employee.stuff)
# print(hermione.stuff)#
