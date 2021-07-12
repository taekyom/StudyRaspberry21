n = 1
name = 'Lee'
n = n + 2
value = 1.2 * n

# print('{0} = 1.2 * {1}'.format(value, n))
# print(name)

# 문자(배열) 인덱스 방법
greeting = 'Hello World!'
print(greeting[0]) #H
print(greeting[2:5]) #llo
print(greeting[:2]) #l
print(greeting[-2:]) #ld

numbers = [0, 1, 2, 3]
print(numbers)
print(numbers[0])
print(numbers[2:5])
names = ['kim', 'lee', 'park', 'choi']
array = numbers + names
print(array)
print(array[-1])
print(array * 2)
array[3] = 7
print(array)

#tuple
person = ('kim', 24, 'female')