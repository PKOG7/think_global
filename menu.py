# MENU
class Menu:
    def __init__ (self, about_us, classroom, community, library, pin_board, results, fees, certification):
        self.about_us = about_us
        self.classroom = classroom
        self.community = community
        self.library = library
        self.pin_board = pin_board
        self.results = results
        self.fees = fees
        self.certification = certification

    def menu():
        print ("SILICON \n 1. About Us 2. Classroom 3. Community 4. Library 5. Pinboard 6. Results 7. Fees 8. Certification ")  
        choice = int(input("Select menu"))

        if choice == 1:
            print("\n This is about us")
        
        elif choice == 2:
            print("1. lecture Slides \n 2. Notes \n 3. COURSE Outline \n 4. Time Table \n 5. Live Class")

        elif choice == 3:
            print("Welcome to the Silicon Chat App")

        elif choice == 4:
            print("\n 1. Kaggle \n 2. Geek for Geek \n 3. Git Hub \n 4. Find \n 5. Youtube ")


        else:
            print("Select Menu above")

        
        # choice = ""

        # while choice != "c" and choice != "f":
        #     choice = input("Choose between 1 to 8")

        #     if choice == "c":
        #         print(int(choice))


    # def menu():
    #     choice = ''  # Start with a wrong answer for choice

    #     while choice != 'c' and choice != 'f':  # Keep asking the user for the right answer
    #         choice = input('Please enter c to encode/decode text, or f to perform frequency analysis: ')

    #     if choice == 'c':
    #         print('Running your message through the cypher…')
    #         message = 'my secret message'
    #         code = atbash(message)
    #         print(code)

    #         # Start up
    # def main():
    #     create_code()
    #     # print(atbash('Test'))
    #     menu()

    menu()
        