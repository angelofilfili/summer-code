class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hello I'm {self.name}, I got a {self.grade}")
        pass

    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False
        
Angelo = Student('Angelo', 90)
Andrew = Student('Andrew', 40)
Jerry = Student('Jerry', 50)

Angelo.introduce()
print(Angelo.is_passing())

Andrew.introduce()
print(Andrew.is_passing())

Jerry.introduce()
print(Andrew.is_passing())

