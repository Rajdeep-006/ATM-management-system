from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def check_bal(self):
        pass
    @abstractmethod
    def withdrawl(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
class New_ATM(ATM):
    def __init__(self,card,pin,bal):
        self.card=card
        self.pin=pin
        self.bal=bal
    
    def check_bal(self):
            attempt=3
            while attempt>0:
                cpin=int(input('Enter the pin: '))
                if cpin==self.pin:
                    print(self.bal)
                    break
                else:
                    print('Incorrect pin')
                    attempt-=1
            else:
                print('Out of attempts')
    def withdrawl(self):
        attempt=3
        while attempt>0:
            cpin=int(input('Enter the pin to withdraw: '))
            if cpin==self.pin:
                amount=int(input('Enter the amount to withdraw: '))
                if amount<=self.bal:
                    self.bal -=amount
                    print('Withdrawn successfully!')
                    print(f'Current balance is {self.bal}')
                    break
                else:
                    print('insufficient balance')
            else:
                print('Incorrect pin')
                attempt-=1
        else:
            print('Out of attempts')

    def deposit(self):
        attempt=3
        while attempt>0:
            cpin=int(input('Enter the pin to deposit: '))
            if cpin==self.pin:
                amount=int(input('Enter the amount to deposit: '))
                if amount<=self.bal:
                    self.bal +=amount
                    print('Depositted successfully!')
                    print(f'Current balance is {self.bal}')
                    break
            else:
                print('Incorrect pin')
                attempt-=1
        else:
            print('Out of attempts')

    def run(self):
        print('choose option- \n1 to check balance\n2 to withdraw\n3 to deposit')
        choice=int(input('Enter choice: '))
        if choice==1:
            self.check_bal()
        elif choice==2:
            self.withdrawl()
        elif choice==3:
            self.deposit()
        else:
            print('Invalid input')
ob=New_ATM(1234567890,6432,20000)
ob.run()

