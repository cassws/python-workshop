### Variables

# Python stores data into variables

myNumber = 4
myWord = "dog"

# Each variable type behaves a little differently.
# For example, you can "print" or display to console
# text data, or what we call a "string"

print(myWord) # the print() function successfully outputs the string

# However, if you try to print out an integer
# Python produces an error

print(myNumber) # Python expects to print a string, so this produces an error

# Luckily, we can switch back and forth between most data types
# As needed.

print(str(myNumber)) # converts myNumber to a text string using str()
# and then prints the output using print(). Success!

# Integers have special properties, too. We can modify the variable
# or "reassign" a value just by using the equqals sign

myNumber = 200

print(str(myNumber))

# We can also modify myNumber by a set amount

myNumber = myNumber + 40

# Python has a shortcut for this using "+="

myNumber += 40

print(str(myNumber))

###  Input and output

# Python starts with the segment of the code to the right
# of the equals sign. In this case, it pauses a moment
# to ask the user for input, prompting with the string
# we "pass" into the function 

myFavoriteAnimal = input("What is your favorite type of animal?")

print(myFavoriteAnimal)

### Control structures

# One of the more powerful features of any programming language
# is the use of if-then statements and other conditions
# For example, let's say we want to accomplish something specific
# if myFavoriteAnimal is a dog

if(myFavoriteAnimal == "dog"):
    print("woof!")

# Note the double equals sign within the if statement
# This is because we don't want to change or reassign the value
# Of myFavoriteAnimal. Instead, we want to check if it is equal
# To the string to the right
# If this condition is satisfied, the code after the colon will execute

# Let's say we want to check for a few different conditions.
# We can use if in conjunction with elif or else to check for other scenarios

if(myFavoriteAnimal == "cat"):
    print("meow!")
elif(myFavoriteAnimal == "cow"):
    print("moo!")
else:
    print("I'm not sure what to say, to be honest.")

### Iteration
# Iteration is another extremely common feature. This allows us
# to repeat a certain activity a set amount of times. In this lesson
# we will be writing a variety of "loops" to accomplish tasks

myLimit = 10
myCounter = 0 # counters allow us to measure how many iterations
# of a loop have passed

while x < 10:
    print("Jump!")
    myCounter += 1
    # What do you think will happen?
