def greet(name="sunbeam"):
    print("Hello,", name)

greet("Vaibhav")
greet()

def student_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student_info(age=18, city="Pune", name="Rahul")

def add(a, b):
    return a + b

def operate(red, v, t):
    return red(v,t)

result = operate(add, 10, 20)
print("Result:", result)


