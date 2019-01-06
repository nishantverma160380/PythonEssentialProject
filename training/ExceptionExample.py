'''

Created On Jan 6, 2019

'''

from os.path import sys

if __name__ == '__main__':
    try:
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        result = num1 / num2
    except ZeroDivisionError:  # Known error
        print("Invalid number entered as input ZeroDivisionError")
    except ValueError:  # Known error
        print("Invalid number entered as input ValueError")
    except:  # For those error which are not specified
        print("Unexpected Error: ", sys.exc_info())
    else:  # Execute this if no error occurred
        print("Division of " + str(num1) + " and " + str(num2) + " is " + str(result))
    finally:
        print("Try catch finally, for closing or finalizing resources using try")
    print("Program completed successfully")  # will be executed if all the error are caught
