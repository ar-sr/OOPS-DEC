class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        
        
        
    def student_input(self):
        self.name=input("enter the your name:")
        self.mark=input("enter your mark:")
        print(self.name,self.mark)
        
        
        
class parent(student):
    def parent_input(self):
        print("iam parent")
        
        
class teacher(parent):
    def teacher_input(self):
        print("iam teacher")
        
        
        
obj1=teacher("","")
obj1.student_input()
obj1.parent_input()
obj1.teacher_input()
        
        
        
