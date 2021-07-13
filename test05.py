import time
import Person

# 클래스 객체
number = [10, 20, 30]
print(dir(number))

p = Person.Person('Lee', 26)
print(p.age)
print(p.name)
print(p.getAge())
print(p.total)

John = Person.Person("John Doe", 35)
print(John.name)