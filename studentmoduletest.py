#this python file is used to test all functionality insidethe student class
#in future that class will be used in real scenario like login/registration 
from modules.student.student import student_details
#step1 : student registration test

email = input("enter your email: ")
password = input("enter your password: ")   

s1=student_details()
s1.setusernameandpassword(email, password)