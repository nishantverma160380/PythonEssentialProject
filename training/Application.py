'''

Created On Jan 5, 2019

'''


class Employee(object):
    # Class level variable
    max_leaves = 40

    # Public method
    def __init__(self, params):
        if (params['empno'] < 0):
            raise Exception("Invalid number input for the employee number" + str(params['empno']))
        self.empno = params['empno']
        self.name = params['name']
        self.salary = params['salary']

    # Method with class level variable
    def displayInfo(self):
        print('EmpNo: ' + str(self.empno) + ' Name: ' + str(self.name) + ' Salary: ' + str(self.__process_salary(30)))
        print("MAX Leaves " + str(self.max_leaves))

    # Class level method
    @classmethod
    def set_max_leaves(cls, number):
        cls.max_leaves = number

    # Private Method
    def __process_salary(self, days):
        return self.salary * days

    def get_salary(self):
        return self.__process_salary(30)

    # Static Method of the class
    @staticmethod
    def read_employee_from_file(fileName):
        print("Read employee object from file : " + fileName)

    def __str__(self, *args, **kwargs):
        return "Employee: Empno: " + str(self.empno) + " Name: " + str(self.name) + " Salary: " + str(self.salary)


class SalesEmployee(Employee):

    def __str__(self, *args, **kwargs):
        return "Sales " + Employee.__str__(self, *args, **kwargs) + " Commission: " + str(
            self.commission) + " Target: " + str(self.target)

    def __init__(self, params):
        Employee.__init__(self, params)
        self.commission = params['commission']
        self.target = params['target']

    def displayInfo(self):
        # Employee.displayInfo(self) can use the existing base class implementation or you can completely override the method
        print('EmpNo: ' + str(self.empno) + ' Name: ' + str(self.name) + ' Salary: ' + str(
            self.get_salary()) + ' Commission: ' + str(self.commission) + ' Target: ' + str(self.target))

    def get_salary(self):
        return Employee.get_salary(self) + (self.commission * Employee.get_salary(self))
