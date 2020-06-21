class Student:  # factory

    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return f'{self.get_full_name()}, Age: {self.age}'

    def inc_age(self, age=1):
        # self.age += 1
        self.age = self.age + age

    # WRONG
    # def info(self, first_name, age):
    #     return f'First Name: {first_name}, Age: {age}'

#################################################################

stud1 = Student('Dima', 'Kaminskyi', 'adwawd')

stud1.inc_age(2)
stud1.inc_age()
print(stud1.age)
