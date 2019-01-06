import unittest
from training.Application import Employee
import os


class TestFileAccess(unittest.TestCase):

    def setUp(self):
        print("SetUp test env")
        pass

    def tearDown(self):
        print("Release test env")
        # os.remove("EmpData.bin")
        pass

    def testReadEmployeeFromFile(self):
        self.emps = Employee.read_employee_from_file("EmpData.bin")
        self.assertGreater(len(self.emps), 0, "No Emp Record Found")
        print("Employee Found from the file")
        for emp in self.emps:
            print(emp)
        pass

    def testWriteEmployeeToFile(self):
        self.emps = Employee.read_employee_from_file("EmpData.bin")
        prevCount = len(self.emps)
        Employee.write_employee_to_file("EmpData.bin", Employee(
            {"empno": int(input("Enter Empno:")), "name": input("Enter Name:"),
             "salary": float(input("Enter Salary:"))}))
        self.emps = Employee.read_employee_from_file("EmpData.bin")
        self.assertGreater(len(self.emps), prevCount, "Could Not write emp detail to file")
        pass

    def testGetEmployeesFromDB(self):
        self.emps = Employee.read_employees_from_table()
        self.assertGreater(len(self.emps), 0, "No Emp Record Found")
        print("Employee Found From database")
        for emp in self.emps:
            print(emp)

    def testEmployeeInDB(self):
        self.emps = Employee.read_employees_from_table()
        prevCount = len(self.emps)
        Employee.add_employee_to_table(Employee({"empno": int(input("Enter Empno for DB:")), "name": input("Enter Name for DB:"),
                                                 "salary": float(input("Enter Salary for DB:"))}))
        self.emps = Employee.read_employees_from_table()
        self.assertGreater(len(self.emps), prevCount, "Could Not write emp detail to file")
        pass
