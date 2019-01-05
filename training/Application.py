'''

Created On Jan 5, 2019

'''

class Employee(object):

    max_leaves=40


    def __init__(self,params):
        self.empno = params['empno']
        self.name = params['name']
        self.salary = params['salary']

    def displayInfo(self):
        print('EmpNo: '+str(self.empno)+' Name: '+str(self.name)+' Salary: '+str(self.__process_salary(30)))
        print("MAX Leaves "+str(self.max_leaves))

    @classmethod
    def set_max_leaves(cls,number):
        cls.max_leaves=number

    def __process_salary(self,days):
        return self.salary*days
