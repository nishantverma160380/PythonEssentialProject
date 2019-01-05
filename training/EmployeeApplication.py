from training.Application import Employee

if __name__ == '__main__':
    emp = Employee({"empno":1000,"name":"Sameer","salary":23456})
    emp.displayInfo()
    # emp.__process_salary(22) private attribute (-__) methods con not be accessed
    print(emp.__str__())

    Employee.set_max_leaves(20)
    # Setting the value in class level variable
    # should not use emp.set_max_leaves(20)

    emp1 = Employee({"empno":1001,"name":"Meer","salary":45678,"d":1})
    emp1.displayInfo()

    emp2 = Employee({"empno":1002,"name":"Sam","salary":12345})
    emp2.displayInfo()

    pass