class Person(object):

    total = 0

    def __init__(self, name, age): #기본 생성자(self)/오버로
        self.name=name
        self.age=age

    def getAge(self):
        return self.age 

class Man(Person):
    gender = 'male'           
class Korean(Person):
    nationality = 'Korea'

class KoreanMan(Man, Korean):
    pass
