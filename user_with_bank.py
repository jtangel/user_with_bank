
class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance, acctType): 
        self.int_rate = int_rate
        self.balance = balance
        self.acctType = acctType
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient funds: this bank is nice and will not charge you')
        else: self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance {self.acctType}: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self



    @classmethod
    def print_all_instances(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.savings = BankAccount(int_rate= 0.2, balance = 2000, acctType= 'savings')
        self.checking = BankAccount(int_rate = 0, balance = 1500, acctType= 'checking')

    def display_info(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")

    def enroll(self):
        self.gold_card_points = 200
        if self.is_rewards_member == True:
            print('User is already member')
        else: self.is_rewards_member = True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('Not enough points for this purchase')
        else: self.gold_card_points -= amount

    def make_deposit(self, amount, acctType):
        if acctType == 'checking':
            self.checking.deposit(amount)
        if acctType == 'savings':
            self.savings.deposit(amount)

    def make_withdrawal(self, amount, acctType):
        if acctType == 'checking':
            self.checking.withdraw(amount)
        if acctType == 'savings':
            self.savings.withdraw(amount)
    
    def display_user_balance(self, acctType):
        if acctType == 'checking':
            self.checking.display_account_info()
        if acctType == 'savings':
            self.savings.display_account_info()
        if acctType == 'total':
            self.checking.display_account_info()
            self.savings.display_account_info()
            totalFunds = self.savings.balance + self.checking.balance
            print(f'Total Funds All Accounts: {totalFunds}')
    



Jack = User('Jack', 'Tangel', 'jackmtangel@gmail.com', 24)

Jack.make_withdrawal(100, 'checking')
Jack.make_deposit(1500, 'savings')
Jack.display_user_balance('total')
