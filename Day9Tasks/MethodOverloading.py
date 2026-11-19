"""7. Student Result Generator (Method Overloading Concept)
A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subjects"""
class Student:
    def __init__(self,s,s2,s3=None):
        self.s=s
        self.s2=s2
        self.s3=s3
    def subjects_sum(self):
        if self.s3 is None:
            return self.s+self.s2
        else:
            return self.s+self.s2+self.s3
a=Student(30,20)
print("2 Subjcets ",a.subjects_sum())
b=Student(30,30,40)
print("3 Subjects ",b.subjects_sum())

 
