class Grade:

    grade_count = 0
    sum_grade = 0
    def __init__(self,student_name, grade, topic):
        self.__student_name = student_name
        self.__grade = grade
        self.__topic = topic
        Grade.grade_count += 1
        Grade.sum_grade += self.__grade

    @staticmethod
    def get_avg(grade_count, sum_grade):
        return f' avg = ({sum_grade} / {grade_count})'

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,new_grade):
        if new_grade < 0 or new_grade > 100:
            print('this is not a real grade! not changing')
            return
        self.__grade = new_grade

    @property
    def topic(self):
        return self.__topic

    @topic.setter
    def topic(self,new_topic):
        if new_topic != 'math' or new_topic != 'python' or new_topic != 'english':
            print('this topic iis not exist')
        self.__topic = new_topic
        
    @property
    def student_name(self):
        return self.__student_name
        
        
        
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#         self.pie = 3.14
#
#     def get_area(self,radius):
#         return  self.pie * self.radius ** 2
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return
# from datetime import datetime
# class Customer():
#
#     current_id = 1
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         self.id = Customer.current_id
#
#
#     @staticmethod
#     def get_current_id():
#         return Customer.current_id
#
#     @staticmethod
#     def reset_id():
#         Customer.current_id += 1
#
#
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)

# class Person:
#
#     def __init__(self, id, name, age):
#         self.__id = id
#         self.__name = name # name must be at least 4 characters
#         self.__age = age # PRIVATE
#         self.__temperature = 90
#
#
#     @property
#     def id(self):
#         return self.__id
#
#
#     def set_age(self, new_age):
#         if (new_age < 0):
#             print('negative age is invalid. I am not changing!!!!')
#             return
#         self.__age = new_age
#
#     # getter - gets a private attribute value interpreted
#
#     @property
#     def name(self):
#         return f'*{self.__name}*'
#
#     @name.setter
#     def name(self, new_name):
#         if len(new_name) < 4:
#             print('too short! dahh')
#             return
#         self.__name = new_name
#
#
#     # getter - gets a private attribute value
#     def get_age(self):
#         return self.__age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)        
