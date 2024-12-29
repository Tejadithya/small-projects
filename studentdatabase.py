class attendence:
    def __init__(self, name, age, gender,attendence):
        self.name = name
        self.age = age
        self.gender = gender
        self.attendence=attendence
    def display(self):
        if self.name=='tej':
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            print(f"Attendence: {self.attendence}")
        print('your name how are you')
    def attend(self):
        print(f"{self.name} is attending the class")
    
    def increment(self,amount):
        self.attendence += amount
        print(f"updated attendence: {self.attendence}")
        
#person1=attendence('tej',12,'male',50)
#person1.display()
#person1.increment(50)

class student:
    def __init__(self,id,studentname,studentamount):
        self.id=id
        self.studentname=studentname
        self.studentamount=studentamount
    def displays(self):
        print('student details')
        print('id',self.id)
        print('name',self.studentname)
        print('amount',self.studentamount)
    def increment(self,amount):
        print('current balance',self.studentamount)
        self.studentamount+=amount
        print('total balance:',self.studentamount)


fucj=student(3,'tejadithya',1000)
fucj.displays()
fucj.increment(500)


