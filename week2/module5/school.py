class student:
    def __init__(self,name,curr_class,id):
        self.name = name
        self.id = id
        self.curr_class = curr_class
    def __repr__(self) ->str:
        return f'Student Name: {self.name},class: {self.curr_class}, id: {self.id}'
    
class teacher:
    def __init__(self,name,subject,id) ->None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) ->str:
        return f'Teacher: {self.name},subject: {self.subject}'
    
class school:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        new_teacher = teacher(name,subject,id)
        self.teachers.append(new_teacher)
    def enroll(self,name,fee):
        if fee < 6500:
            return 'Not Enough Fee'
        else:
            id = len(self.students) + 1
            new_student = student(name,'C',id)
            self.students.append(new_student)
            return f'{name} is enrolled with id: {id}, extra money {fee-6500}'

    def __repr__(self)->str:
        print('Welcome to',self.name)  
        print('------OUR Teachers-------')
        for teacher in self.teachers:
            print(teacher)
        for student in self.students:
            print(student)
            return 'ALL Done'


#mahidi = student('mahidi',10,1)
#MHB = Teacher('MHB','Algorithm',101)
#print(mahidi)
#print(MHB)

phitron = school('Phitron')
phitron.enroll('Mahidi',5200)
phitron.enroll('Siam',6200)
phitron.enroll('Asif',7000)

phitron.add_teacher('Rifat Ahmed','Algorithm')
phitron.add_teacher('MHB','Data Structure')
phitron.add_teacher('Mahbub','Java')

print(phitron)
