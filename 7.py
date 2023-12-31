# . Write a program that takes a string as input and checks if it is a palindrome
# (reads the same forwards and backwards)
inp_string = input("Enter the string to check weather its is palindrom or note")
revese_string = inp_string[::-1]
if inp_string == revese_string:
    print("Given string is palindrom ")
else:
    print("Given string is not palindrom ")
