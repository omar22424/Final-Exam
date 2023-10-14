class User():
    
    accounts = []
    account_number = 10000
    isBankrupt = False
    isLoanActive = True
    

    def __init__(self, name, email, address, accType) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.accType = accType
        self.balance = 0
        self.loanTaken = 0
        self.accountNumber = str(User.account_number)
        User.account_number += 1
        self.trans_history = []
        self.loan_taking = 0
        User.accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        history = f'An ammount of {amount} taka has been deposited into your account'
        self.trans_history.append(history)

    def withdrew(self, amount):
        if amount > self.balance:
            print("You don't have enough balance.")
        elif self.isBankrupt == True:
            print("You can't withdraw money. The is Bankrupt.")
        else:
            history = f'An ammount of {amount} taka has been withdrawed from your account'
            self.balance -= amount
            self.trans_history.append(history)

    def check_balance(self):
        print("Your avilable balance is: TK.", self.balance)

    def transaction_history(self):
        print(self.trans_history)


    def take_loan(self, amount):
        if self.loan_taking < 2 and self.isLoanActive == True:
            print(f'An amount of {amount} taka loan has been given to you.')
            history = f'An ammount of {amount} taka has been taken as loan.'
            self.trans_history.append(history)
            self.loanTaken += amount
            self.loan_taking += 1
        elif self.loan_taking == 2:
            print("You have taken loan twice. You can't take loan anymore.")
        elif self.isLoanActive == False:
            print("The bank has stopped giving loan.")

    
    def transfer_money(self, reciever_account_number, amount):
        for reciever in User.accounts:
            if reciever.accountNumber == reciever_account_number:
                if amount <= self.balance:
                    self.balance -= amount
                    reciever.balance += amount
                else:
                    print("Insufficient balance for the transfer.")
                break
        else:
            print("Account does not exist.")


class Admin():

    def create_account(self, name, email, address, accType) -> None:
        User(name, email, address, accType)

    def delete_account(self, user_account_number):
        check = 0
        for acc in User.accounts:
            if acc.accountNumber == user_account_number:
                print(f'Account of Name: {acc.name} and Acoount Number: {acc.accountNumber} has been deleted.')
                User.accounts.remove(acc)
                check += 1
        if check == 0:
            print(f'Your provided account number does not exist.')

    def see_all_user_account_list(self):
        for user in User.accounts:
            print(f"Account Number: {user.accountNumber}, Name: {user.name}, Email: {user.email}, Address: {user.address}, Account Type: {user.accType}")

    def total_bank_balance(self):
        balance = 0
        for acc in User.accounts:
            balance += acc.balance
        print("Total balance of the bank: TK.", balance)

    def total_loan_given(self):
        balance = 0
        for acc in User.accounts:
            balance += acc.loanTaken
        print("Total loan given from the Bank: TK.", balance)

    def loan_off(self):
        User.isLoanActive = False
        print("Loan taking is off now.")

    def loan_on(self):
        User.isLoanActive = True
        print("Loan taking is on now.")

    def bankrupt(self):
        User.isBankrupt = True
        print("An admin shut down withdrawel of money.")




while(True):
    
    print("""Select any option - 
1) Create account (By User)
2) Open Admin Panel
3) Exit from the system""")
    
    option = input()

    if option == '1':
        print("Insert the following Informarion:")
        name = input("Name: ")
        email = input("Email: ")
        address = input("Address: ")
        accType = input("Account Type: ")
        user = User(name, email, address, accType)
        print(f'Your Account Name: {user.name}, Account Number: {user.accountNumber}')
        print("""Select any option -
1) Deposit money
2) Withdraw money
3) Check available balance
4) Check Transaction History
5) Take Loan
6) Transfer money to other account
7) End Task""")
        while(True):
            task = input("Enter your Choice: ")
            if task == '1':
               amount = input("Enter the amount you want to Deposit: ")
               user.deposit(int(amount))
               continue
            if task == '2':
               amount = input("Enter the amount of money you want to withdraw: ")
               user.withdrew(int(amount))
               continue
            if task == '3':
               user.check_balance()
               continue
            if task == '4':
              user.transaction_history()
              continue
            if task == '5':
               amount = input("Enter the amount of loan you want to take: ")
               user.take_loan(int(amount))
               continue
            if task == '6':
               accNum = input("Enter reciever's account number: ")
               amount = input("Enter the amount of money: ")
               user.transfer_money(accNum, int(amount))
               continue
            if task == '7':
               break
        
    if option == '2':
        admin = Admin()
        print("Admin Panel is Open.")
        print("""Select your Option -
1) Create Account for a User
2) Delete any user account
3) See all user account
4) Check total bank balance
5) Check total Loan
6) Loan off
7) Loan on
8) Bankrupt the bank
9) End Task""")
        while(True):
            task = input("Enter your Choice: ")
            if task == '1':
                print("Take the following detail from the User for opening an account.")
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                accType = input("Account Type: ")
                admin.create_account(name, email, address, accType)
   
            if task == '2':
               acc = input("Enter user account number: ")
               admin.delete_account(acc)
               continue
            if task == '3':
               admin.see_all_user_account_list()
               continue
            if task == '4':
               admin.total_bank_balance()
               continue
            if task == '5':
               admin.total_loan_given()
               continue
            if task == '6':
               admin.loan_off()
               continue
            if task == '7':
               admin.loan_on()
               continue
            if task == '8':
               admin.bankrupt()
               continue
            if task == '9':
                break
        
    if option == '3':
        break    
