# ENCAPSULATION 

try:
    class BankAccount:
        def __init__(self):
            self.name = "John"         # public
            self._balance = 5000       # protected
            self.__pin = 1234          # private

        def show_account(self):
            print("Name:", self.name)
            print("Balance:", self._balance)
            print("PIN is hidden")

    account = BankAccount()

except Exception as e:
    print(e)

else:        
    # Public → easy access
    print(account.name)

    # Protected → you can access, but not recommended
    print(account._balance)

    # Private → cannot access directly
    # print(account.__pin)  

finally:
    print("ENCASPULATION DONE!!")