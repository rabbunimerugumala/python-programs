# 	CREATING STUDENT DATA

student_data = []


def create_student(filename):
    n = int(input("\nEnter The Count Of The Students: "))
    for i in range(n):
        # print("Enter The Student(Name,RollNo,Branch,Section,PhoneNumber,Email) : ")
        print(f"\nEnter {i + 1} Student Data:- ")

        name = input("\tName Of The Student        : ")
        rollno = input("\tRollNo Of The Student    : ")
        branch = input("\tBranch Of The Student    : ")
        section = input("\tSection Of The Student  : ")
        phno = input("\tPhoneNumber Of The Student : ")
        email = input("\tEmail Of The Student      : ")
        student_data.append(f"{name.title()},{rollno},{branch},{section},{phno},{email} ")
    f = open(filename, "a+")
    f.writelines(student_data)
    f.close()

# READING STUDENT DATA
def read_student(filename):
    f = open(filename, "r+")
    data = f.readlines()
    for line in data:
        word = line.split(",")
        print(word)
    f.close()


# DELETING THE STUDENT DATA
def delete_student(filename):
    inp_roll_no = input("Enter The Roll Number To Delete: ")
    f = open(filename, "r+")
    data = f.readlines()
    f.close()
    for index, line in enumerate(data):
        roll_no = line.split(",")[1]
        if inp_roll_no == roll_no:
            data.pop(index)
            print(f"student with {roll_no} deleted successfully")

    f = open(filename, 'w+')
    f.writelines(data)
    f.close()


# UPDATING THE STUDENT DATA
def update_student(filename):
    inp_roll = input("Enter The Roll Number To Update: ")
    f = open(filename, "r+")
    data = f.readlines()
    f.close()
    for index, line in enumerate(data):
        name, roll_no, branch, section, phone_no, email = line.split(",")
        if inp_roll == roll_no:
            if input("Do you want update name: ") == "y":
                upd_name = input("Enter The Name To Update: ")
            else:
                upd_name = name

            if input("Do you want update Branch: ") == "y":
                upd_branch = input("Enter The Branch To update: ")
            else:
                upd_branch = branch

            if input("Do you want update Section: ") == "y":
                upd_section = input("Enter The Section To update: ")
            else:
                upd_section = section

            if input("Do you want update Phone Number: ") == "y":
                upd_phone_no = input("Enter The Phone Number To update: ")
            else:
                upd_phone_no = phone_no

            if input("Do you want update Email: ") == "y":
                upd_email = input("Enter The Email To update: ")
            else:
                upd_email = email

            data[index] = f"{upd_name},{roll_no},{upd_branch},{upd_section},{upd_phone_no},{upd_email}"

            f = open(filename, 'w+')
            f.writelines(data)
            f.close()

            print("*** Students Data Updated SuccessFully ***")

# TO GET THE TOTAL COUNT OF STUDENTS
def getTotalStudentCount(filename):
    f = open(filename, "r+")
    data = f.readlines()
    return len(data)


def memu():
    print("			+------------------------------------------------+")
    print("			|   STUDENT MANAGEMENT SYSTEM    |")
    print("			+------------------------------------------------+")
    print(" 1. ADD NEW STUDENT.".title())
    print(" 2. GET All STUDENT DETAILS.".title())
    print(" 3. UPDATE THE STUDENT DETAILS.".title())
    print(" 4. DELETE STUDENT.".title())
    print(" 6. GET STUDENT DETAILS.".title())
    print(" 7. NUMBER OF STUDENTS IN SCHOOL.".title())
    print(" 8. Exit..")
    print()


# MAIN FUNCTION
if __name__ == '__main__':
    filename = "data\\student.txt"
    while True:
        memu()
        option = int(input(" >> Enter Any Above Given Option:- "))
        print()
        if option == 1:
            create_student(filename)

        elif option == 2:
            if option == 2:
                f = open(filename, "r+")
                data = f.readlines()
                print("  \t**Total Number of Students In School:-", getTotalStudentCount(filename))
                print("\n\t*** Total Students List With The Details ***\n")
                for sNo,student in enumerate(data):
                    print(" >> Student- ", sNo + 1)
                    read_student(filename)
                    print()
            else:
                print("\tNo Students There!")
        elif option == 3:
            update_student(filename)
        elif option == 4:
            # delete_student(filename)
            inp_roll_no = input("Enter The Roll Number To Delete: ")
            f = open(filename, "r+")
            data = f.readlines()
            f.close()
            for index, line in enumerate(data):
                roll_no = line.split(",")[1]
                if inp_roll_no == roll_no:
                    try:
                        data.pop(index)
                        print(f"student with {roll_no} deleted successfully")
                        f = open(filename, 'w+')
                        f.writelines(data)
                        f.close()
                    except:
                        print("\t\tNo Student There To Delete..")

        elif option == 8:
            exit()

