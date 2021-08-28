import sys
import os


class User:  # Parent Class Holds details about an user
    def __init__(self, name, age, gender, idn, word, balance=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
        self.idn = idn
        self.word = word

    def user_details(self):   # Function to show user's details
        print('--- User Details ---')
        print(f'Name: {self.name.capitalize()}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender.capitalize()}')
        print(f'ID: {self.idn}')
        print(f'pssword: {self.word}')


class Bank(User):  # Child Class Inherits details from parent class
    def __init__(self, name, age, gender, idn, word):
        super().__init__(name, age, gender, idn, word)

#
    def deposits(self, amount):   # Function to add money and show balance
        Bank.word(self)
        self.amount = amount
        self.balance += self.amount
        print(f"--- Transition has been done ---!\nCurrent balance is: $ {self.balance}")

    def withdraw(self, amount):   # Function to take money and show balance
        Bank.word(self)
        self.amount = amount
        if self.amount > self.balance:  # Here to compare first with exist balance
            print(f"'Sorry! Amount is bigger than current balance'\nCurrent Balance Is: $ {self.balance}")
        else:
            self.balance -= self.amount
            print(f"--- Transition has been done! ---\nCurrent Balance Is: $ {self.balance}")

    def view_balance(self):  # Function to show balance
        Bank.word(self)
        print(f'Current Balance Is: $ {self.balance}')

    def word(self):  # Function asks to enter password and check it with original password
        while True:
            pword = input("Enter your 5 digits Password: ")
            if not pword.isdigit() or len(pword) != 5 or pword != self.word:
                print("--- Wrong Password!, Please re-enter right Password ---")
                continue
            else:
                break

    def main_function(self):  # Function to run Transitions according to user's choices
        while True:
            print("---------- Transitions ----------")
            print("1.To show all details account")
            print("2.To show account balance ")
            print("3.To show withdraw")
            print("4.To show deposit")
            print("5.To Sign Out")
            print("0.To exit from the system")

            ask = input("Enter your choice number: ")
            if not ask.isdigit():
                print("Wrong choice!, Please re-enter right number from above")
                continue
            if int(ask) == 1:
                Bank.user_details(self)
            elif int(ask) == 2:
                Bank.view_balance(self)
            elif int(ask) == 3:
                try:
                    amount = int(input("Enter withdraw amount: "))
                    Bank.withdraw(self, amount)
                except:
                    print("Wrong Insert!, Please re-enter integer number")
                    continue
            elif int(ask) == 4:
                try:
                    amount = int(input("Enter deposit amount: "))
                    Bank.deposits(self, amount)
                except:
                    print("Wrong Insert!, Please re-enter integer number")
            elif int(ask) == 0:
                print("Thanks For Your Banking With Us")
                sys.exit()
            elif int(ask) == 5:
                print("************** Sign out **************")
                print("--- Sign In Again --- ")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("Wrong choice!, Please re-enter right number from above")
                continue


# User's interface script to enter data to the programme


print("***** Welcome To Our Bank ******\n*** Bank Account Creator ***")

while True:  # Loop to get user's name

    name = str((input("Type Your Name: ")))
    if not name.isalpha():
        print("Wrong Name.. Insert Alphabet")
        continue
    else:
        break

while True:  # Loop to get user's age
    age = (input("Enter Your Age: "))
    if not age.isdigit():
        print("Wrong Age, Please insert Right age")
        continue
    else:
        break

while True:  # Loop to get user's gender
    gender = input("Enter Your Gender ( m/f ): ")
    if gender.lower() == 'm' or gender.lower() == 'f':
        break
    else:
        print("Please insert 'm' or 'f'")
        continue

while True:  # Loop to get user's ID
    idn = (input("Enter Your ID: "))
    if not idn.isdigit():
        print("Wrong ID, Please insert Digit ID")
        continue
    else:
        break

while True:  # Loop to get user's Password
    word = input("Enter your 5 digits Password: ")
    if not word.isdigit() or len(word) != 5:
        print("Wrong Password!, Please re-enter right Password")
        continue
    else:
        break

print("Thanks.... Account Has been Created")
print("*********************************************")
user = Bank(name, age, gender, idn, word)

while True:  # Loop to check if user would like to go on or exit the programme
    ask = input("Would you like to perform Transaction? (y/n): ")
    if ask == "y".lower():
        user.main_function()
    elif ask == "n".lower():
        print("Thanks For Banking With Us")
        break
    else:
        print("Wrong Choice! Please enter 'y' or 'n'")




























