class Employees:

    def __init__(self, emp_ID, emp_name, dept, salary):
        self.emp_ID = emp_ID
        self.emp_name = emp_name
        self.dept = dept
        self.salary = salary

    
    
    def display(self):
        print("\n-----Employee Details-----")
        print("Employee ID: ",self.emp_ID)
        print("Employee Name: ",self.emp_name)
        print("Department of employee: ",self.dept)
        print("Salary of employee: ",self.salary)

    
    
    def emp_detail(self):
        return f"{self.emp_ID},{self.emp_name},{self.dept},{self.salary}"
    
    
    
    
            
            
