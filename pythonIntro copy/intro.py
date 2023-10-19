
# Comments
#  variables

name = "Ricky"
last_name = "Array"
age = 34
price = 100000000000000000.99
found = False

print(name + " " + last_name)
print("My age is:" + str(age))


# conditionals

if age < 100:
    print("Don't worry you're still young")
    print("still inside the if")
elif age == 100:
    print("Congrats on the century!")
else:
    print("Sorry, but you're old")

print("outside the if") 


def say_hello():
    print("Hello from a function")


def sum(num1,num2):
    total = num1 + num2
    print("the result is" + str(total))

def division(num1, num2):
    if num2 == 0:
        print("Mistake")
    else:
        result = num1 / num2
        print(result)

def greet(name):
    print("hello" + name)

def print_greater(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)


greet("Billionaire")
say_hello()
sum(-2, 345)
sum(21, 21)
division(100, 10)
division(10, 2)
division(100, 0)
print_greater(9, 6)
print_greater(3, 6)