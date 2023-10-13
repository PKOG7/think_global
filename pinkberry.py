# KELVIN OFFEH-GYIMAH

# CREATING AN APP FOR POS SYSTEM

# CLASSES NECESSARY FOR POS
class Visa:
    def __init__(self):
        self.logo = ""

    def card_credibility(self):
        return True
    pass
    
class Mastercard:
    def __init__(self):
        self.logo = ""

    def card_credibility(self):
        return True
    pass
    
class Bank(Visa, Mastercard):
    def __init__(self) -> None:
        super().__init__
    def balance():
        return "balance"
    
    def withdrawal():
        return "withdrawal"
    
    def pay_in():
        return "pay in"

    def transaction_confirmation():
        return "transaction confirmation"
    pass

class Ecobank(Bank):
    def __init__(self, bank_account_name, bank_account_number):
        super().__init__()
        self.bank_account_name = bank_account_name
        self.bank_account_number = bank_account_number
    
    def card_credibility():
        return True
    
    def balance():
        return
    
    def withdrawal():
        return
    
    def pay_in():
        return

    def transaction_confirmation():
        return
    
    pass

class Standard_Chartered(Bank):
    def __init__(self, bank_account_name, bank_account_number):
        super().__init__()
        self.bank_account_name = bank_account_name
        self.bank_account_number = bank_account_number

    def card_credibility(self):
        return True
    
    def balance(self):
        return
    
    def withdrawal(self):
        return
    
    def pay_in(self):
        return

    def transaction_confirmation(self):
        return
    pass

class Absa(Bank):
    def __init__(self, bank_account_name, bank_account_number):
        super().__init__(bank_account_name, bank_account_number)
        self.bank_account_name = bank_account_name
        self.bank_account_number = bank_account_number

    def card_credibility():
        return True
    
    def balance():
        return
    
    def withdrawal():
        return
    
    def pay_in():
        return

    def transaction_confirmation():
        return
    pass
    
    
        
class debit(Absa, Ecobank, Standard_Chartered):
    def __init__(self, bank_account_name, bank_account_number, card_number, card_pin):
        super().__init__(bank_account_name, bank_account_number)
        self.card_number = card_number
        self.card_pin = card_pin

    def pin_check(pin):
        return

    def balance(self):
        return
    
    def withdrawal(self):
        return

    def pay_in (self):
        return
    
    def transaction_confirmation(self):
        return super().transaction_confirmation()
    
    def pin_check(self):
        if pin == self.card_pin:
            print("You entered a valid pin")
            return True
        else:
            print("Wrong Pin. Please enter a valid pin")
        return  False
    pass

user_bank = input("What bank do you bank with: ")

while user_bank.upper() == "ECOBANK":
    card_type = input("Is your card a credit card or a debit card?\n Please enter 'c' for credit card or 'd' for debit card")
    if card_type.lower() == "c":
        account_number = input("Please type in your account number: \n")
    #if account_number == credit.card_number:
        try:
            pin = int(input("Please enter your pin: "))
        except ValueError:
            print("Please enter numbers pin not a letter")
        else:
            print("Congratulations")

while user_bank.upper() == "ABSA":
    card_type = input("Is your card a credit card or a debit card?\n Please enter 'c' for credit card or 'd' for debit card")
    if card_type.lower() == "c":
        account_number = input("Please type in your account number: \n")
    #if account_number == credit.card_number:
        try:
            pin = int(input("Please enter your pin: "))
        except ValueError:
            print("Please enter numbers pin not a letter")
        else:
            print("Congratulations")

while user_bank.upper() == "STANDARD CHARTERED BANK":
    card_type = input("Is your card a credit card or a debit card?\n Please enter 'c' for credit card or 'd' for debit card")
    if card_type.lower() == "c":
        account_number = input("Please type in your account number: \n")
    #if account_number == credit.card_number:
        try:
            pin = int(input("Please enter your pin: "))
        except ValueError:
            print("Please enter numbers pin not a letter")
        else:
            print("Congratulations")




class credit(Absa, Ecobank, Standard_Chartered):
    # card_number = ""
    def __init__(self, bank_account_name, bank_account_number, card_number, card_pin):
        super().__init__(bank_account_name, bank_account_number)
        self.card_number = card_number
        self.card_pin = card_pin

        #card_number =int(card_number*10)
    
    def pin_check(pin):
        return
    
    def balance(self):
        return
    
    def withdrawal(self):
        return
    
    def pay_in(self):
        return
    
    def transaction_confirmation(self):
        return super().transaction_confirmation()
    pass


user_bank = input("What bank do you bank with: ")
while user_bank.upper() == "ECOBANK":
    card_type = input("Is your card a credit card or a debit card?\n Please enter 'c' for credit card or 'd' for debit card")
    if card_type.lower() == "c":
        account_number = input("Please type in your account number: \n")
    #if account_number == credit.card_number:
        try:
            pin = int(input("Please enter your pin: "))
        except ValueError:
            print("Please enter numbers pin not a letter")
        else:
            print("Congratulations")
            break

while user_bank.upper() == "ABSA":
    card_type = input("Is your card a credit card or a debit card?\n Please enter 'c' for credit card or 'd' for debit card")
    if card_type.lower() == "c":
        account_number = input("Please type in your account number: \n")
    #if account_number == credit.card_number:
        try:
            pin = int(input("Please enter your pin: "))
        except ValueError:
            print("Please enter numbers pin not a letter")
        else:
            print("Congratulations")
            break

while user_bank.upper() == "STANDARD CHARTERED BANK":
    card_type = input("Is your card a credit card or a debit card?\n Please enter 'c' for credit card or 'd' for debit card")
    if card_type.lower() == "c":
        account_number = input("Please type in your account number: \n")
    #if account_number == credit.card_number:
        try:
            pin = int(input("Please enter your pin: "))
        except ValueError:
            print("Please enter numbers pin not a letter")
        else:
            print("Congratulations")
            break

            # if pin == credit.card_pin:
            #     credit.withdrawal()
            # pass

# print(pin)

kwame = credit("Kwame Osei-Owusu","0001234560","0923451000","7890")
print(kwame.card_pin)