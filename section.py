#1 Define a class to represent companies. Companies will have a name 
#(given at creation), a list of all sales for the year string of a product, 
#and a dictionary of products (strings, keys) and their prices (float like, values), 
#as well as a list of employees
# #2 Define a 
#function to add a new product. The function will take the name of the product and the price.  
#3 Define a function to add an employee, given an employee.
# def someFunc(): class MyClass:

class Companies():
    
    def __init__(self, name, sales, product, prices, employees):
        self.__name = name
        self.__sales = sales[]
        self.__product = product{}
        self.__prices = float(prices)
        self.__employees = employees #should be list passed in 
    
    def get_name(self):
        return self.__name
    
    def get_sales(self):
        return self.__sales

    def get_product(self):
        return self.__sales

    def get_prices(self):
        return self.__prices
    
    def get_employees(self):
        return self.__employees
    
    def add_product(self, name, price):
        self.__product[name] = self.__prices
        #__add__(self, product, price)
    
    def add_employee(self, emp_name)
        self.__employees.append(emp_name)