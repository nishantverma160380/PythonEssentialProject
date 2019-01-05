'''

Created On Jan 5, 2019

'''

class Employee(object):

    def __init__(self,params):
        self.empno = params['empno']
        self.name = params['name']
        self.salary = params['salary']

    def displayInfo(self):
        print('EmpNo: '+str(self.empno)+' Name: '+str(self.name)+' Salary: '+str(self.salary))
