from training.Application import Employee, SalesEmployee
from os.path import sys

if __name__ == '__main__':

    try:
        emp = Employee({"empno": 1000, "name": "Sameer", "salary": 23456})
        emp.displayInfo()
        # emp.__process_salary(22) private attribute (-__) methods con not be accessed
    except:
        print("Exception Occurred: ", sys.exc_info())
    else:
        print(emp.__str__())
        print(emp)
        emp.displayInfo()

    Employee.set_max_leaves(20)
    # Setting the value in class level variable
    # should not use emp.set_max_leaves(20)

    try:
        emp1 = Employee({"empno": -1001, "name": "Amer", "salary": 45678})
        emp1.displayInfo()
    except:
        print("Exception Occurred: ", sys.exc_info())
    else:
        print(emp1.__str__())
        print(emp1)
        emp1.displayInfo()

    emp2 = Employee({"empno": 1002, "name": "Sam", "salary": 12345})
    emp2.displayInfo()

    Employee.read_employee_from_file("empData.dat")

    sales_emp2 = SalesEmployee({"empno": 1003, "name": "Ram", "salary": 123456, "commission": 0.5, "target": 30000})
    sales_emp2.displayInfo()

    print(sales_emp2.__str__())
    print(emp2.__str__())

    print(sales_emp2)
    print(emp2)

    print(isinstance(emp, Employee))

    pass
