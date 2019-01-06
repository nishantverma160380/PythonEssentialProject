'''

Created On Jan 5, 2019

'''

from os.path import sys
import pickle
from mysql.connector import connect

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
    @classmethod
    def read_employee_from_file(cls, fileName):
        print("Read employee object from file : " + fileName)
        try:
            cls.emps_from_file = []
            currentFile = open(fileName, "rb")
            cls.emps_from_file = pickle.load(currentFile)
            currentFile.close()
        except:
            print("Exception Occurred: ", sys.exc_info())
            cls.emps_from_file = []
        finally:
            return cls.emps_from_file

    @classmethod
    def write_employee_to_file(cls, fileName, newEmp):
        #print("Write employee object to file : " + fileName)
        try:
            cls.emps_from_file = Employee.read_employee_from_file(fileName)
            cls.emps_from_file.append(newEmp)
            currentFile = open(fileName, "wb")
            pickle.dump(cls.emps_from_file, currentFile)
            currentFile.close()
        except:
            print("Exception Occurred: ", sys.exc_info())

    @classmethod
    def read_employees_from_table(cls):
        ctx = connect(user="root", password="password", database="training", port=3306)
        cursor = ctx.cursor()
        cursor.execute("select * from emp_data")
        cls.emps = []
        for (empno, name, salary) in cursor:
            cls.emps.append(Employee({"empno": empno, "name": name, "salary": salary}))
        cursor.close()
        ctx.close()
        return cls.emps

    @classmethod
    def add_employee_to_table(cls, newEmployee):
        ctx = connect(user="root", password="password", database="training", port=3306)
        cursor = ctx.cursor()
        cursor.execute("insert into emp_data values (%s,%s,%s)",
                       (newEmployee.empno, newEmployee.name, newEmployee.salary))
        ctx.commit()
        print("Employee Inserted Successfully ")
        cursor.close()
        ctx.close()

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
