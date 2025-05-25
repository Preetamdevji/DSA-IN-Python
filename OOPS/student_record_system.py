from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self,name,roll_no,marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
    
    def getName(self):
        return self.__name
        
    def getRollNo(self):
        return self.__roll_no
      
    def getMarks(self):
        return self.__marks
    
    @abstractmethod
    def show_data(self):
        pass
        
class ComputerScienceStudent(Student):
    def __init__(self, name, roll_no, marks, branch):
         super().__init__(name, roll_no, marks)
         self.branch = branch  

    def show_data(self):
        print("👨‍💻 Computer Student Information:")
        print(f"Name   : {self.getName()}")
        print(f"Roll No: {self.getRollNo()}")
        print(f"Marks  : {self.getMarks()}")
        print(f"Branch : {self.branch}")      


class EngineeringStudent(Student):
    def __init__(self, name, roll_no, marks, specialization):
        super().__init__(name, roll_no, marks)
        self.specialization = specialization

    def show_data(self):
        print("👨‍💻 Engineering Student Information:")
        print(f"Name   : {self.getName()}")
        print(f"Roll No: {self.getRollNo()}")
        print(f"Marks  : {self.getMarks()}")
        print(f"Branch : {self.specialization}")


class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self,student_obj):
        self.students.append(student_obj)

    def show_all_students(self):
        for student in self.students:
            student.show_data()

    def search_by_roll(self, roll_no):
        for student in self.students:
            if student.getRollNo() == roll_no:
                return student
        return None

    def sort_by_marks(self):
        self.students.sort(key=lambda student: student.getMarks(), reverse=True)
        

    def sort_by_name(self):
        self.students.sort(key= lambda student: student.getName())



mgr = StudentManager()
mgr.add_student(ComputerScienceStudent("Amit", 101, 85, "AI"))
mgr.add_student(EngineeringStudent("Ravi", 102, 90, "Mechanical"))

mgr.show_all_students()

found = mgr.search_by_roll(102)
if found:
    print("\n🔍 Found Student:")
    found.show_data()
