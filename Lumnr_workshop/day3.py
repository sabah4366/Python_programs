import re
# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# string="ABCDEFabcdef123450"
# char = re.compile(r'[^a-zA-Z0-9]')
# string = char.search(string)
# if not bool(string):
#     print("True")
# else:
#     print("False")

 
# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
# txt="hai my name is sabah"

# if re.search("b*",txt):
#     print("matched")
# else:
#     print("not matched")



# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.
# txt="hai my name is sabah"
# ptrn='[^A-Z]+_'
# s=re.match(ptrn,txt)
# if s:
#     print("found")
# else:
#     print("not found")

# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# txt="ai my Ame is sabah"
# ptrn='[A-Z]+[a-z]'
# s=re.search(ptrn,txt)
# if s:
#     print("found")
# else:
#     print("not found")

# 5. Write a Python program that matches a word containing 'z', not  at the start or end of the word.
# txt="zai my name is sabah".split()
# for strng in txt:
#     if re.search(r'\Bz',strng):
#         print("found")
#     else:
#          print("not found")


# 6.Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# dt=input("enter the date like  yyyy-mm-dd format")
# year,month,day=dt.split('-')
# print(f"dd-mm-yyyy format:{day}-{month}-{year}")


# 7.Write a Python program to split a string with multiple delimiters.
# strng="hai my Name *is #sabah "
# obj=re.split(r':|,|\*|\#',strng)
# print(obj)

# 8.Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument
#  student_name or student_class the function will print the student name and class.
# def student_data(student_id,**kwargs):
#     print(f"student id :{student_id}")
#     if 'student_name'  in kwargs:
#         print(f"student name : ${kwargs['student_name']}")

#     if 'student_name' and 'student_class' in kwargs:
#         print(f"\nstudent name : ${kwargs['student_name']}")
#         print(f"student  class : ${kwargs['student_class']}")
        
# student_data(student_id=12,student_name="sabah",student_class="plustwo")
# student_data(student_id=12,student_name="sabah")


# 20. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like
#     calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# • Use 'assign_department' method to change the department of an employee.
# • Use 'print_employee_details' method to print the details of an employee.
# • Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by
#  the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary.
#  Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))
# class Employee():
#     def __init__(self,emp_id,emp_name,emp_salary,emp_dept):
#         self.id=emp_id
#         self.name=emp_name
#         self.salary=emp_salary
#         self.dept=emp_dept

#     def calculate_emp_salary(self,salary,hrs_worked):
#         overtime=0
#         if hrs_worked>50:
#             overtime=hrs_worked-50
#         self.salary=self.salary+(overtime*(self.salary/50))    
        

        

#     def emp_assign_department(self,new_dept):
#         self.dept=new_dept

#     def print_employee_details(self):
#         print("Id of the employee:",self.id)
#         print("Name of the employee:",self.name)
#         print("Salary of the employee:",self.salary)
#         print("Department of the employee:",self.dept)
#         print("---------------------------------------------")

# #object creating for the class
# emp1=Employee(10,"sabah",50000,"Python Developer")
# emp2=Employee(11,"safwan",60000,"Golang Developer")
# emp3=Employee(12,"nadeem",55000,"MEARN Stack")
# emp4=Employee(13,"sulaim",45000,"MEAN Stack")

# #original Employee details
# emp1.print_employee_details()
# emp2.print_employee_details()
# emp3.print_employee_details()
# emp4.print_employee_details()

# #department changing
# emp1.emp_assign_department("DataScience")
# emp4.emp_assign_department("Machine Learning")

# #calculte the overtime working hours
# emp1.calculate_emp_salary(50000,58)
# emp2.calculate_emp_salary(600000,6)


# #details of after the dept changing and calculate overtime working 
# emp1.print_employee_details()
# emp2.print_employee_details()
# emp3.print_employee_details()
# emp4.print_employee_details()


    


# 1. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods
#  like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
#     • Now add items to the menu.
#     • Make table reservations.
#     • Take customer orders.
#     • Print the menu.
#     • Print table reservations.
#     • Print customer orders.
# Note: Use dictionaries and lists to store the data
class Restaurant():
    def __init__(self) :
        self.menu_items={}
        self.book_table=[]
        self.cust_order=[]


    def add_item_to_menu(self,item,price):
        self.menu_items[item]=price
        
    def book_tables(self,tab_no):
        self.book_table.append(tab_no)
        
    def customer_order(self,order):
        self.cust_order.append(order)

    def print_menu(self):
        for key,val in self.menu_items.items():
            print(key,val)

    def print_table_reservations(self):
        for tabl in self.book_table:
            print(tabl)
    def print_cust_orders(self):
        for ord,tbl in zip(self.cust_order,self.book_table):
            print(f"Table No:{tbl}\tOrder:{ord}")


#object created to Restaurant class  
res=Restaurant()


#added items
res.add_item_to_menu("CB",150)
res.add_item_to_menu("BB",250)


#Book tablles
res.book_tables(13)
res.book_tables(12)

#ordered
res.customer_order("Cb")
res.customer_order("Bb")


print("show menu")
res.print_menu()


print("Show Table Reservations")
res.print_table_reservations()


print("Show order and table")
res.print_cust_orders()