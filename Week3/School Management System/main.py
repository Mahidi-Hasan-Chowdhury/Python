from school import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom

school1 = School('ABC',"Dhaka")

eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school1.add_classroom(eight)
school1.add_classroom(nine)
school1.add_classroom(ten)


rahim = Student("Rahim",eight)
karim = Student("Karim",nine)
fahim = Student("Fahim",ten)
hamim = Student("Hamim",ten)


school1.student_admission(rahim)
school1.student_admission(karim)
school1.student_admission(fahim)
school1.student_admission(hamim)


abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")


bangla = Subject("Bangla",abul)
physics = Subject("Physics",babul)
chemistry = Subject("Chemistry",kabul)
biology = Subject("Biology",kabul)
math = Subject("Math",babul)


eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_final_exam()
nine.take_final_exam()
ten.take_final_exam()
print(school1)