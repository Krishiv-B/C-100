class Atm:
    def __init__(self):
        self.AtmCarnNumber=int(input("Enter your ATM card Number: "))
        self.PinNUmber=int(input("Enter your PIN Number: "))
        self.balance=0 
        print("Account Made!")
        DepositAmount=int(input("Enter the amount to be deposited: "))
        self.balance=DepositAmount+self.balance
        print("Yay! Your balance is now: ", self.balance)
        AmountWithdrawn=int(input("Enter the amount to be withdrawn: "))
        if self.balance>=AmountWithdrawn:
            self.balance= self.balance-AmountWithdrawn
            print("The balance is: ", self.balance)
        else:
            print("Invalid Withdrawal")
    
        
   
        

acc =Atm()

