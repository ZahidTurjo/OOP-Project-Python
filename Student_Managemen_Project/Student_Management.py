class StudentDatabase:
    students_list=[]
    
    @classmethod
    def add_student(self,student):
        self.students_list.append(student)
    
    # def student_veiw(self):
    #     return self.students_list
        


class Student:
    def __init__(self,student_id,name,department):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=False

        StudentDatabase.add_student(self)
    
    def get_id(self):
        return self.__student_id
    
    def enroll_student(self):
        if self.__is_enrolled==False:
            self.__is_enrolled=True
            print(f"{self.__name} is successfully enrolled")
        
        else:
            print(f"Error: {self.__name} is already enrolled")
    
    def drop_student(self):
        if self.__is_enrolled==False:
            print(f"Error: {self.__name} is not Enrolled")
        else :
            self.__is_enrolled = False
            print(f"{self.__name} has been dropped")

    def view_student_info(self):
        print(f"Student_id:{self.__student_id},Name:{self.__name},Department:{self.__department} ,Enroll_status:{self.__is_enrolled}")


# s1=Student(1,"ok","ok")
# s2=Student(2,"ok","ok")
# for x in StudentDatabase.students_list:

#     x.view_student_info()

s1=Student(1,"Turjo","Applied Math")
s2=Student(2,"Zahidul","CSE")
s3=Student(3,"Sami","EEE")

while True:
    print('\n Student Management System')
    print("1: Veiw All Studenst Info")
    print("2: Enroll student")
    print("3: Drop Student")
    print("4: Exit")
    

    choice=int(input("Enter your Choice[1-4] :"))

    if(choice==1):
        print("Lsit of ALL Students")
        for student in StudentDatabase.students_list:
            student.view_student_info()
    elif choice==2:
        stud_id=int(input('Enter Student Id To Enroll:'))
        found=False
        
        for student in StudentDatabase.students_list:
            if(stud_id== student.get_id()):
                student.enroll_student()
                found=True
                break
        if found==False:
            print(f'Error: {stud_id} id is invalid')
    
    elif choice==3:
        stud_id=int(input('Enter Student Id To Enroll:'))
        found=False
        
        for student in StudentDatabase.students_list:
            if(stud_id== student.get_id()):
                student.drop_student()
                found =True
                break
        if found==False:
            print(f'Error: {stud_id} id is invalid')      

            
    elif choice==4:
        print("Exist The Management System")
        break

    else:
        print("Invalid Choice.Choice Between [1-4]")

