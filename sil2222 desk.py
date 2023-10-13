import getpass
import datetime

class School:
    def __init__(self,school):
        self.school = "Silicon"
    
    def sign_up():

        while True:
            #first_name = input("Enter your first name: ")
            try:
                student.first_name = first_name
                first_name = input("Enter your first name: ")
                # last_name = input("Enter your first name: ")
                # email = input("Enter your first name: ")
                # student = Student(first_name, last_name, email)
                # newAdmissions = Admissions(student, school)
                first_name1 = first_name.isalpha()
                if first_name1 == True:
        
                    #pass
                    print(first_name)
                    break

                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

            # this is for last name
        while True:
            try:
                #student.last_name = last_name
                last_name = input("Enter your last name: ")
                last_name1 = last_name.isalpha()
                if last_name1 == True:
                
                    print(last_name)
                    break
                    #pass
                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

            # this is for dob

        # while True:
        #     try:
        #         dob = input("Enter your date of birth: ")
        #         dob = dob.datetime(2023, 5,6)



        while True:
            try:
                #student.email = email
                email= input("Enter your e-mail: ")
                condition = "@"
                if condition in email:
                    print(email)
                    break
                else:
                    print("Please enter a valid email address")
            except ValueError:
                print("Enter valid name")
        
        while True:
            try:
                #student.password = password
                password1 = getpass.getpass("Create a password: ")
                password1_valid = any(chr.isdigit() for chr in password1)
                if password1_valid == True:
                    print("Strong")
                else:
                    print("Weak Password: Include Numbers")
                
                password2 = getpass.getpass("Confirm your password: ")
                password2_valid = any(chr.isdigit() for chr in password2)
                if password2 == True:
                    print("Strong")
                else:
                    print("Weak Password: Include Numbers")
                break

            except ValueError:
                print("Invalid Input")
                


        print(f"Your first name is {first_name}, \n Your last name is {last_name}, \nYour email is{email}")       
            
            
        #last_name  = input("What is your last name: ")

    def log_in():
       
       #this is for the email

        while True:
            try:
                #student.email = email
                email= input("Enter your e-mail: ")
                condition = "@"
                if condition in email:
                    print(email)
                    break
                
            except ValueError:
                print("Enter a valid email address")
                


            #this is for the password

        while True:
                try:
                    #student.password = password2
                    password2 = getpass.getpass("Enter your password: ")
                    password2_valid = any(chr.isdigit() for chr in password2)

                    if password2 == True:
                        print("confirmed")
                    else:
                        print("Wrong password")
                    break

                except ValueError:
                    print("Invalid Input")
                



class Student:
    def __init__(self,first_name,last_name,email,course,password,dob,gender,student_id,contact):
        self.first_name = first_name
        self.last_name  = last_name
        self.email = email
        self.course = course
        self.password = password
        self.dob = dob
        self.gender = gender
        self.student_id = student_id
        self.contact = contact
    
    # def sign_up():
    #     while True:
    #         #first_name = input("Enter your first name: ")
    #         try:
    #             student.first_name = first_name
    #             first_name = input("Enter your first name: ")
    #             # last_name = input("Enter your first name: ")
    #             # email = input("Enter your first name: ")
    #             # student = Student(first_name, last_name, email)
    #             # newAdmissions = Admissions(student, school)
    #             first_name1 = first_name.isalpha()
    #             if first_name1 == True:
        
    #                 #pass
    #                 print(first_name)
    #                 break

    #             else:
    #                 print("Please try again")
    #         except ValueError:
    #             print("Enter valid name")

    #         # this is for last name
    #     while True:
    #         try:
    #             #student.last_name = last_name
    #             last_name = input("Enter your last name: ")
    #             last_name1 = last_name.isalpha()
    #             if last_name1 == True:
                
    #                 print(last_name)
    #                 break
    #                 #pass
    #             else:
    #                 print("Please try again")
    #         except ValueError:
    #             print("Enter valid name")

    #         # this is for dob

    #     # while True:
    #     #     try:
    #     #         dob = input("Enter your date of birth: ")
    #     #         dob = dob.datetime(2023, 5,6)



    #     while True:
    #         try:
    #             #student.email = email
    #             email= input("Enter your e-mail: ")
    #             condition = "@"
    #             if condition in email:
    #                 print(email)
    #                 break
    #             else:
    #                 print("Please enter a valid email address")
    #         except ValueError:
    #             print("Enter valid name")
        
    #     while True:
    #         try:
    #             #student.password = password
    #             password1 = getpass.getpass("Create a password: ")
    #             password1_valid = any(chr.isdigit() for chr in password1)
    #             if password1_valid == True:
    #                 print("Strong")
    #             else:
    #                 print("Weak Password: Include Numbers")
                
    #             password2 = getpass.getpass("Confirm your password: ")
    #             password2_valid = any(chr.isdigit() for chr in password2)
    #             if password2 == True:
    #                 print("Strong")
    #             else:
    #                 print("Weak Password: Include Numbers")
    #             break

    #         except ValueError:
    #             print("Invalid Input")
                


    #     print(f"Your first name is {first_name}, \n Your last name is {last_name}, \nYour email is{email}")       
            
            
    #     #last_name  = input("What is your last name: ")


    # def log_in():
       
    #    #this is for the email

    #     while True:
    #         try:
    #             #student.email = email
    #             email= input("Enter your e-mail: ")
    #             condition = "@"
    #             if condition in email:
    #                 print(email)
    #                 break
                
    #         except ValueError:
    #             print("Enter a valid email address")
                


    #         #this is for the password

    #     while True:
    #             try:
    #                 #student.password = password2
    #                 password2 = getpass.getpass("Enter your password: ")
    #                 password2_valid = any(chr.isdigit() for chr in password2)

    #                 if password2 == True:
    #                     print("confirmed")
    #                 else:
    #                     print("Wrong password")
    #                 break

    #             except ValueError:
    #                 print("Invalid Input")
                


        #print(f"Your first name is {first_name}, \n Your last name is {last_name}, \nYour email is{email}")  

    def course(self,innovation_school,innovation_studio,start_up_funding,software_development,data_engineering,innovation_partnership):
        #if
        pass
        return
    
    def pay_fees():
        return
    
#student = Student()
#Student.sign_up()

Student.log_in()

student = Student()
