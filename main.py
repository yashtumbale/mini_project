from employee import Employees
from file_handler import save_employee,read_employee
from analytics import *
from random_data import generate_random_employee


while True:
    print("\n-----CHOICES-----")
    print("1: Add new employee")
    print("2: Generate random employees")
    print("3: Search employee")
    print("4: View employees")
    print("5: Salary analytics")
    print("6: Salary Increment")
    print("7: Department analysis")
    print("8: Filter employees based on salary")
    print("9: Exit!")
    choice = input("Enter choice: ")
    
    if choice == "1":
        try:
            emp_ID = int(input("Enter emloyee ID: "))
            name = input("Enter employee name: ")
            dept = input("Enter employee department: ")
            salary = int(input("Enter employee salary:"))

            if salary < 0:
                raise ValueError("Salary cannot be negative.")
            
            s1 = Employees(emp_ID,name,dept,salary)
            s1.display()
            save_employee(s1.emp_detail())
        except ValueError as e:
            print(e)
        

    elif choice == "2":
        generate_random_employee()


    elif choice == "3":
        search_emp()


    elif choice == "4":
        read_employee()


    elif choice == "5":
        salary_analytics()

        
    elif choice == "6":
        increment_salary()


    elif choice == "7":
        department_analytics()


    elif choice == "8":
        filter_emp()


    elif choice == "9":
        print("Succesfully Exit!")
        break


    else:
        print("Please enter valid choice!")

