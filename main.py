print('Hello, Python.')
print(2001)
print("What","do","commas","do?")
print("Does", "adding",      "space", "matter?")
print('Launch' + 'Code')
print("LaunchCode \n was founded in", 2013)
#forward slash n for new line
print("----------")
print("GUI - graphic user interface is a system designed with icons and visual representations of the machines files")
print("--------------")
print("CLI - command line interface uses textual commands to give computer instructions. apps running the CLI are terminals adn the program interpreting the commands are call the shell")
print("the absolute path is the path to a file from the root directory \n and the relative path is the path to a file from the current directory")
print("-----------")
print(type('hello. an EXPRESSION returns a VALUE'))
print('-------------------------')
print("floor division (//) returns the whole number of the equotient while the modulus operator (%) returns the remainder")

print("-----order of operations: parenthases; exponentiation; mulitplication, division, modulus evaluated left to right; addition and subtraction evaluated left to right ------")
# the right-most ** operator is applied first
print(2 ** 3 ** 2)

# use parentheses to force the order you want
print((2 ** 3) ** 2)
print("-----------user input------")
user = input("please enter your name:")
print("hello " + user +'!')
num1 = input("enter a number:")
num2 = input("enter a second number:")
print(num1 +num2)
print(int(num1) + int(num2))
print(type(user))
