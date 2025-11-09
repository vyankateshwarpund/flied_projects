# A program to input a number and display the same number in hexadecimal and binary format.
num = int(input("Enter a number:"))
#for print hexadecimal
hexadecimal = hex(num)
#for print binary
binary = bin(num)
print("Hexadecimal of a number is {}:" .format(hexadecimal))
print("Binary of a number is {}:" .format(binary))
