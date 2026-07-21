import numpy as np
from employee import Employees


salary = []
with open("data.txt", "r") as file:

    for line in file:

        emp = line.strip().split(",")

        salary.append(int(emp[3]))

salary = np.array(salary)

def update_salary(salary):
    employees = []

    with open("data.txt","r") as file:
        for line in file:
            employees.append(line.strip().split(","))

    for i in range(len(employees)):
        employees[i][3] = str(int(salary[i]))

    with open("data.txt","w") as file:
        for emp in employees:
            file.write(",".join(emp) + "\n")


def salary_analytics():
    
    avg_salary = np.mean(salary)
    max_salary = np.max(salary)
    min_salary = np.min(salary)
    median_salary = np.median(salary)
    std_salary = np.std(salary)

    print("Average salary of employees: ",avg_salary)
    print("maximum salary of employee: ",max_salary)
    print("minimum salary of employee: ",min_salary)
    print("Median salary of employees: ",median_salary)
    print("Standared deviation salary of employees: ",std_salary)



def increment_salary():
    salary = []
    with open("data.txt", "r") as file:
        for line in file:
            emp = line.strip().split(",")
            salary.append(int(emp[3]))

    salary = np.array(salary)

    
    print("1: Increment by Percentage")
    print("2: Increment by Amount")
    
    Choice = int(input("Enter your choice for increment: "))
    
    if Choice == 1:
    
        n =int(input("Enter percentage of increment (%): "))
    
        salary = salary+(salary * (n/100))
        print("Increment salary by percentage succesfuly!")
    
    
    elif Choice == 2:
    
        n = int(input("Enter amount to increment salary: "))

        salary = salary + n
        print("Increment salary by amount succesfuly!")
    
    else:
    
        print("Choice is incorrect")

    update_salary(salary)


    



def department_analytics():

    print("IT")
    print("HR")
    print("sales")
    print("Finance")
    print("Marketing")

    dept = input("Enter choice: ")

    with open("data.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[2] == dept:

                print("ID:", data[0])
                print("Name:", data[1])
                print("Department:", data[2])
                print("Salary:", data[3])
                print("------------------")

        
            
def search_emp():
    emp_id = input("Enter emp_ID of employee for searching: ")
        
        
    with open("data.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == emp_id:

                print("ID:", data[0])
                print("Name:", data[1])
                print("Department:", data[2])
                print("Salary:", data[3])
                print("------------------")


def filter_emp():
    e_l_f = []
    e_g_f =[]
    with open("data.txt", "r") as file:
        for line in file:
            emp1 = line.strip().split(",")
            if emp1[3] <= "50000":
                e_l_f.append(emp1)

            else:
                e_g_f.append(emp1)

    print("Employees with less than 50000 salary: ")
    print(e_l_f)
    print("\nEmployees with greater than 50000 salary: ")
    print(e_g_f)
    
