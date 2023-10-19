# functions

def exc1():
    print("=== List ===")

    names = ["Patience", "Kennedy"]
    print(names)

    # add elements
    names.append("Ricky")
    names.append("Dexter")

    # read elements
    print(names[0])
    print(names[2])

    # check if an element exists
    if "KJ" not in names:
        names.append("KJ")

    # travel with for loop
    for name in names:
        print(name)


def exc2():
    numbers =[12,3,53,67,12,8,45,87,31,98,30,82,24,16,82,68,34]

# 1 print every number
    print(numbers)

# 2 print how many elements there are in the list
    count = len(numbers)
    print("There are " + str(count) + " numbers in the list")

# 3 sum of all numbers
# 4 how many numbers are greater than 250
# 5 how many are equal or lower than 100

    total = 0
    count = 0
    count_low = 0
    for num in numbers:
        total += num

        if num < 50:
            count += 1

        if num <= 100:
            count_low += 1

    print(total)
    print(count)
    print(count_low)


def how_many_times(color):
    colors = ["Red", 'yellow', "BLUE", "RED", "GreeN", "YELLOW", "reD", "green"]
    # how many times the color appears in list
    # parse color to lowercase 
    # for loop
    # if color in lower is equal to cl in lower
    # increase count
    
    count = 0
    for cl in colors:
        if cl.lower() == color.lower():
            count += 1

    print("there are" + str(count) + " occurrences of " + color)

def print_dict():
    me = {
        "name": "Ricky",
        "last": "Array",
        "hobbies": ["Reading", "Gym", "Shopping"]
    }

    print(me)


# call the functions
exc1()
exc2()
print_dict()

how_many_times('red')
how_many_times('GREEN')