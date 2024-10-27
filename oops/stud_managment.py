class Student:

    student_Dictionary = {}
    school_name = "xyz"


    def __init__(self):
        self.name = input("\nName Of The Student: ")
        self.roll_no = input("\nRollNo Of The Student: ")
        branch = input("\nBranch Of The Student: ")
        self.section = input("\nSection Of The Student: ")
        self.phno = input("\nPhoneNumber Of The Student: ")
        self.email = input("\nEmail Of The Student: ")

        if branch in StudentBranch.branches :
            StudentBranch.branches[branch].studentList.append(self)
        else:
            new_branch = StudentBranch(branch)
            new_branch.studentList.append(self)
            StudentBranch.branches[branch] = new_branch
        self.branch = StudentBranch.branches[branch]

        print("\n***Student Added SuccessFully***")
        self.getstudent()

# PRINTING  STUDENT DETAILS
    def getstudent(self):
        print("\n--- STUDENT DETAILS ---\n")
        print("\tName : ",self.name)
        print("\tRollNo : ",self.roll_no)
        print("\tBranch : ",self.branch.name)
        print("\tSection : ",self.section)
        print("\tPhoneNumber : ",self.phno)
        print("\tEmail : ",self.email)

# UPDATING THE STUDENT DETAILS
    def updateStudent(self):
        print("\tSelect Option To Update Student Details..\n")
        print("\t\t1. Change Student Name : ")
        print("\t\t2. Change Student Branch : ")
        print("\t\t3. Change Student Section : ")
        print("\t\t4. Change Student PhoneNumber : ")
        print("\t\t5. Change Student Email : ")

        option = input("\t\tEnter Option To Update: ")
        print()

        if option == ['1','2','3','4','5']:
            if option == '1':
                self.name = input("Enter The Student New Name : ")
                print("\n\t***Student Name Updated SuccessFully***")

            elif option=='2':
                new_branch = input("Enter The Student New Branch : ")
                self.branch.studentList.remove(self)
                try:
                   self.branch  = StudentBranch.branches[new_branch]
                   self.branch.studentList.remove(self)
                except:
                    addbranch = StudentBranch(new_branch)
                    self.branch=addbranch
                    addbranch.studentList.append(self)
                print("\n\t***Student Branch Updated SuccessFully***")

            elif option=='3':
                self.section = input("Enter The Student New Section : ")
                print("\n\t***Student Section Updated SuccessFully***")
            elif option=='4':
                self.phno = input("Enter The Student New PhoneNumber : ")
                print("\n\t***Student PhoneNumber Updated SuccessFully***")
            else:
                self.email = input("Enter The Student New Email : ")
                print("\n\t***Student Email Updated SuccessFully***")
            self.getstudent()

        else :
            print("\n\tYou Have Chosen Wrong Option !")

# METHOD TI=O UPDATE THE SCHOOLNAME..
    @classmethod
    def updateSchoolName(cls,new_schl_name):
        cls.school_name = new_schl_name

# METHOD TO GET ALL STUDENTS IN MANAGEMENT
    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_Dictionary)



class StudentBranch:
    branches = {}
    def __init__(self,name):
        self.name = name
        StudentBranch.branches[name] = self
        self.studentList = []




# MAIN ..
def main():
    print("------------------------------------------------------")
    print(f"|  {Student.school_name} STUDENT MANAGEMENT SYSTEM  |")
    print("------------------------------------------------------")
    print("\t1. GET STUDENT DETAILS..".title())
    print("\t2. ADD NEW STUDENT..".title())
    print("\t3. REMOVE STUDENT..".title())
    print("\t4. UPDATE THE STUDENT DETAILS..".title())
    print("\t5. UPDATE THE SCHOOL NAME.. ".title())
    print("\t6. NUMBER OF STUDENTS IN SCHOOL..".title())
    print("\t7. GET ALL STUDENT DETAILS..".title())
    print("\t8. GET ALL STUDENT DETAILS..".title())

    option = int(input("Enter Any Above Given Option: "))
    print()

    if  option == '1':
        roll_no = input("\tenter the roll number of the student: ".title())
        try:
            Student.student_Dictionary[roll_no].getstudent()
        except:
            print("\t\tYou Have Entered The Wrong Student RollNumber!")

    elif option == '2':
        new_student = Student()
        Student.student_Dictionary[new_student.roll_no] = new_student

    elif option == '3':
        roll_no = input("\tenter the roll number of the student: ".title())
        try:
            student = Student.student_Dictionary.pop(roll_no)
            student.branch.studentList.remove(student)
            print(f"\t\t '{roll_no}' - Student Deleted SuccessFully")
        except:
            print("\t\tNo Student There To Delete..")

    elif option == '4':
        roll_no = input("\tenter the roll number  of the student: ".title())
        print()
        try:
            Student.student_Dictionary[roll_no].updateStudent()
        except:
            print("\t\tYou Have Entered The Wrong Student RollNumber!")


    elif option == '5':
        new_schl_name = input("\tenter the new school name : ".title())
        Student.updateSchoolName(new_schl_name)
        print("***School Name Changed SuccessFully***")

    elif option == '6':
        print("Total Number of Students In School: ",Student.getTotalStudentCount())

    elif option == '7':
        if Student.student_Dictionary:
            print("Total Number of Students In School: ",Student.getTotalStudentCount())
            print("\nTotal Students List With The Details\n")
            for sNo,student in enumerate(Student.student_Dictionary.values()):
                print("Student- ",sNo+1)
                Student.getstudent()
                print()
        else:
            print("\tNo Students There!")

    elif option == '8':
        try:
            students = StudentBranch.branches[input("\tEnter The Branch Name: ")]
            print("\nStudents Of Class- ",students.name)
            print(f"\nTotal Numbers of Students In Class {students.name}: {len(students.studentList)}")
            print()
            for sNo,student in enumerate(Student.student_Dictionary.values()):
                print("Student- ",sNo+1)
                Student.getstudent()
                print()
        except:
            print("\nYou Entered Wrong Name Or No Student There")


if __name__ == '__main__':
    option = "y"
    while option =='y':
        main()
        option = input("\nDo You Want To Continue [y/n]: ")
        print()
