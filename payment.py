class Card:
    def __init__(self,card_number,cvv_number,pin_number,email):
        self.card_number = card_number
        self.cvv_number  = cvv_number
        self.pin_number = pin_number
        self.email = email
        # self.card = card

    def card():
            #CARD NUMBER
            while True:
                
                try:
                    card_number = int(input("Enter your card number: "))
                    card_string = str(card_number)

                    if len(card_string) == 10:
            
                        print(card_number)
                        break

                    else:
                        print("Please try again")
                except ValueError:
                    print("Enter valid number")

            #CVV

            while True:

                try:
                    cvv_number = int(input("Enter the CVV number behind your card: "))
                    cvv_string = str(cvv_number)
                   
                    if len(cvv_string) == 3:
                    
                        print(cvv_number)
                        break

                    else:
                        print("Please try again")
                except ValueError:
                    print("Enter valid CVV number")

            #PIN

            while True:

                try:
                    pin_number = int(input("Enter yor PIN number: "))
                    pin_string = str(pin_number)
                   
                    if len(pin_string) == 4:
                    
                        print("Transaction complete")
                        break

                    else:
                        print("Please try again")
                        
                except ValueError:
                    print("Enter valid PIN number")
                    break

            
            #EMAIL
            while True:
                try:
                    email = input("Email: ")
                    if email in email == True:
                        break
                    else:
                        print("Email does not match")
                
                except ValueError:
                    print("Invalid Input")
Card.card()
