class student:
    def __init__(self,student_name,mark):
        self.student_name=student_name
        self.marks=mark
    school_name="MHS"

    
    @classmethod()
    def display_info(cls):
        print("this is basic info!")


    def display(self):
        print(self.student_name)
        print(self.marks)
        print(self.school_name)

d1=student(102,"noman")
d1.display()


    
        