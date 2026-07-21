
def save_employee(emp):
    
    file = open("data.txt","a")

    file.write(emp +"\n")

    file.close()

    print("Succesfully Saved!")

def read_employee():

    file = open("data.txt","r")

    for line in file:
        print(line)

    file.close()
    print("Succesfully Printed all employees details!")
