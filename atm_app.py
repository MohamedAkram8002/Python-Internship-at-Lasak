class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Please enter your PIN: ")
            if entered_pin == self.pin:
                print("Authentication successful!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.\n")
        print("Authentication failed. Exiting.\n")
        return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}\n")

    def deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.\n")
        else:
            print("Invalid amount. Please enter a positive number.\n")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.\n")
        elif amount > self.balance:
            print("Insufficient funds.\n")
        else:
            print("Invalid amount. Please enter a positive number.\n")

    def run(self):
        if not self.authenticate():
            return
        
        while True:
            print("Welcome to the ATM!")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Please select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    atm = ATM(balance=1000)  # Initialize with a balance of $1000
    atm.run()
