# PythonEssentialProject
Python Essential Training Project


1. Setup for Python Environment
	a. Identify the installer from python.org: downloads
	b. development Environment: Idle(bundled), Eclipse, Anaconda, PyCharm, VSCode
	c. start -> Python CLI: Interactive Python Console [run python scripts]
	d. Eclipse: set the Python Interpretor using Quick Auto Config for Python
	Window -> Preferences -> Python -> Python Interpreter -> New/Browse [pythonpath]
	Window -> Perspective -> Open Perspective -> Other -> PyDev
2. Create the Workspace
	a. Create a Pydev Project :Name
	b. Create a Python Package to group mulitple modules
	c. Create a Python Module: <name>.py
		i. CLI: with options/args for building Python Script
		ii. Main: with main Method to call function and classes
		iii. Class: Create module with Classes grouped together
		iv. UnitTest: test case classes for testing existing modules
3. Programming Constructs
	a. Simple Types: integer,long,float,double	
	b. Sequence Types
		i. String: tuple of characters to group as string
		ii. Tuple: group of objects, immutable once created 
			ex_tuple= (12,3,("Test","Name"),343,44)
		iii. List: group of Object can be mutable
			ex_list = [22,33,("Test","Name"),[23,33],45]
		iv. Dictionary: group of items can be mutable
			ex_dictionary = {"key":"value","main":{"name":"summary"}}
	c. control structures
		Selection: if <condition>: 
				<statements>
			    elif <condition>:
				<statements>
			    else:
				<statements>
		Iteration:   while <condition>: 
				 <statements>
			     for var in iterables:
4. Implementing functional Programming
	a. declaring function
		def <name>(<args>):
			<statements>
			return	\\procedure		
			return expression \\ function
5. Implementing Object Oriented Programming
	a. creating the class module
		class <name>(<base-class>):
			<class variables>
	b.  initializing objects using constructor
		__init__(self,params)
			self.<name> = <value> // instance variable 
	c. initiailizing Object functions
		def <name>(self,arg1,arg2):	
			self.<value> = arg1
	d. declaring class methods
		@classmethod
		def <name>(cls,arg1,arg2):
			cls.<value>= arg1
	e. declaring static method
		@staticmethod
		def <name>(arg1,arg2)
			<statements>
6. Implementing Inheritance 
	a. Using Inheritance in classes
		class <name>(<base-class>,<base-class2>): 
			<statements>
	b. Calling the base Constructor in derived class
		<Base-Class>.__init__(self,params)
	c. Using the Base Class Method definition to Override in Derived Class
		def <method-from-base>(self):
			<base-class>.<method>() 
			<additional statements to override the behavior>
	d. Built in methods for object
		a. __str__(): print the object values
		b. __eq__(value): compare the objects and return boolean value
7. Exception Handling
	a. identify the abnormal condition at runtime as an Exception
	caused using logical error, invalid inputs
	b. All the Internal Errors , Interpretor raises an error 
		ValueError,ZeroDivisionError
	c. Handling the Exception Scenarios
		try:
			<statements which may raise an exception>
		except <Error/Exception>:[n]
			<statements to handle known Exceptions in the code>
		except:
			<statements to handle all other possible exceptions>
		else:
			<statements to execute on successful try block completion>
		finally:
			<statements to execute irrespective of error or success>
	d. Raising our Own Exception
		raise: keyword to raise an new Exception() on business conditions
8. File Handling 
	a. open(<name>,<option>): (r,w,a[b][+])
	b. close(file) : used to close the open file object
	c. Using Pickle library to manage data access
		a. pickle.load(file): load the binary object from the file
		b. pickle.dump(data,file): write/append data to the file 
	d. read(): read multiline text content
	   write(): write/append single or multiline text to the file
9. Unit Test
	a. unittest.TestCase: create class to inherit from TestCase
	b. each test method prefix with test_<scenario>(self)
	c. self.assert<Condition>(actual,expected,message)
	d. Use setup and teardown for inititalizing and releasing objects required for 		each test case executed
10. Data base Connectivity using Python
	1. Identify/ Create the Database Table
	2. Install the connector library using pip to use api in Python
	3. Use connection to connect to the database using database options
		connect(host,port,username,password)
	4. Create the cursor Object and execute the query using the SQL,Parameters
		cursor.execute("insert into emp_data values(%s,%s,%s)",
		(int(input("Empno:")),input("name"),float(input(salary))))
		connection.commit(),cursor/connection.close()
	5. Fetching the data
		execute("select * from emp_data ")
		Fetch each record Fields using the for loop
		for (empno,name,salary) in cursor
			<statements to use the data fetched from the db>




Create Workspace

    a. Create Python Project
    b. Create a Python Package to group multiple modules
    c. Create a Python module which is actually a .py file
        1 CLI
        2 Main
        3 Class
        4 Unit Test


Programming Constructs: data types:
    
    Simple Type:-
        integer, long, flote , double
        
    Sequence Type:-
    
        Python Tuple Methods
    
            In Python, tuple is immutable. You cannot change elements of a tuple once it is assigned. There are only 2 tuple methods that tuple objects can call: count and index. The page contains theses 2 tuple methods. Also the page includes built-in functions that can take tuple as a parameter and perform some task. For example, len() returns the length of a tuple (iterable).
      
            Method	Description
            Python Tuple count()	returns occurrences of element in a tuple
            Python Tuple index()	returns smallest index of element in tuple
            Python any()	Checks if any Element of an Iterable is True
            Python all()	returns true when all elements in iterable is true
            Python ascii()	Returns String Containing Printable Representation
            Python bool()	Converts a Value to Boolean
            Python enumerate()	Returns an Enumerate Object
            Python filter()	constructs iterator from elements which are true
            Python iter()	returns iterator for an object
            Python len()	Returns Length of an Object
            Python max()	returns largest element
            Python min()	returns smallest element
            Python map()	Applies Function and Returns a List
            Python reversed()	returns reversed iterator of a sequence
            Python slice()	creates a slice object specified by range()
            Python sorted()	returns sorted list from a given iterable
            Python sum()	Add items of an Iterable
            Python tuple() Function	Creates a Tuple
            Python zip()	Returns an Iterator of Tuples
  
      Tuple: ('envy', 34, [CMSC], (1,2))          ---------immutable


    Strings:" ", ' ', """ """
    List:[1,2,'name',('q','w')]

    in operator
    t=[1,2,4,5]
    3 in t
    false

   range,
   appand,
   pop,
   insert,
   reverse,
   sort.


    Dictionarirs
        Like map:- {key:value}
        
        keys, values, items
        has_key
        
        keys can be -- number, string, tuple 
        keys should be immutable
        
        
    