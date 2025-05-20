num = input("Enter number: ")
try:
    num1 = int(num)*int(num)
    print("square root number: ", num1)
except ValueError:
    print("Enter only 'int'-numbers")
