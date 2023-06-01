# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:

    no_of_cust = 0
    ac_num = 42011

    def __init__(self, name, gender, age, dob, mob_no,initial_depo):
        self.name = name
        self.gendrer = gender
        self.age = age
        self.dob = dob
        self.mob_no = mob_no
        self.balance = initial_depo

        Bank_Account.ac_num = Bank_Account.ac_num + 1
        Bank_Account.no_of_cust = Bank_Account.no_of_cust + 1



    def basic_details(self):
        print(f'User: {self.name}\t Account No:{self.ac_num}\t Balance: {self.balance}')


    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)

    def payment(self, other):
        amount = int(input("Enter the Payment amount: "))
        if amount <= self.balance and amount > 0:
            self.balance = self.balance - amount
            self.balance = other.balance + amount
            print(f'Current balance : {self.balance}')
        else:
            print('Invalid')

if __name__ == '__main__':

    cust1 = Bank_Account(name='Jenny', gender = 'Female', age= 25, dob=25/2/1996,  mob_no=8190020392, initial_depo=1000)
    cust2 = Bank_Account(name='John',gender='Male', age=30, dob=13/3/1993, mob_no=8056353754, initial_depo=2000)
    print("Hello!!! Welcome to the NPH BANK ")
    print('No.of.customers is', Bank_Account.no_of_cust)
    print(cust1.basic_details())
    cust1.deposit()
    print(cust1.basic_details())
    cust1.withdraw()
    print(cust1.basic_details())
    cust1.payment(cust2)
    print(cust1.basic_details())

    #print(cust2.basic_details())
    #cust2.deposit()
    #print(cust2.basic_details())
    #cust2.withdraw()
    #print(cust2.basic_details())
    #cust2.payment(cust1)
    #print(cust2.basic_details())


