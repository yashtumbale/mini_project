import random


def generate_random_employee(filename="data.txt", number=10):

    names = [
        "Rahul",
        "Amit",
        "Priya",
        "Sneha",
        "Karan",
        "Neha",
        "Rohan",
        "Anjali",
        "Vijay",
        "Pooja",
        "Hari",
        "Ramesh"
    ]

    departments = [
        "IT",
        "HR",
        "Sales",
        "Finance",
        "Marketing"
    ]

    with open(filename, "a") as file:

        for i in range(number):

            emp_id = random.randint(1000, 9999)

            name = random.choice(names)

            dept = random.choice(departments)

            salary = random.randint(25000, 80000)

            file.write(f"{emp_id},{name},{dept},{salary}\n")

    print(number, "Random Employees Added Successfully")
