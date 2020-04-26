# complete this function so that it prints Hello, World
def printHelloWorld() :
    print("Hello, World")

# complete this function so that it prints whatever is provided in the parameter
def printParam(param) :
    print(param)

# complete this function so that it returns the sum of num1 and num2
def sumTwoNumbers(num1, num2) :
     sum = num1 + num2

     return sum

# complete this function so that it returns the square of the num parameter
def findSquare(num) :
    sum = num * num

    return sum

# complete this function so that it returns True if day is Wednesday
# otherwise return False
def dayIsWednesday(day) :
    if day == "Wednesday" :
        return True
    else :
        return False



myList = [ "mainsheet", "batton", "rudder", "foil", "block" ]

# complete this function so that it return "I got it" if item is in myList
# otherwise return "I have to get it"
def findInList(finditem) :
    for item in myList :
        if finditem == item :
            return "I got it"

    return "I have to get it"

# assuming every element in 'numList' is a number, complete this function so that it
# returns the total sum of the elements in the list
def complexSum(numList) :
    sum = numList

    return sum


printHelloWorld()

printParam("sailing")

execute = sumTwoNumbers(5, 16)
print("sumTwoNumbers(5, 16) ", execute)

execute = findSquare(11)
print("findSquare(11) ", execute)

execute = dayIsWednesday("Tuesday")
print('dayIsWednesday("Tuesday") ', execute)

execute = dayIsWednesday("Wednesday")
print('dayIsWednesday("Wednesday") ', execute)

execute = findInList("rudder")
print('findInList("rudder") ', execute)

execute = findInList("quickdraw")
print('findInList("quickdraw") ', execute)

execute = complexSum([1, 3, 5, 7, 9])
print('complexSum([1, 3, 5, 7, 9]) ', execute)

execute = complexSum([2, 4, 6, 8, 10])
print('complexSum([2, 4, 6, 8, 10]) ', execute)