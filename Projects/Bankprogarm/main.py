# Python Banking System..



def show_balance():
    print(f"Your balance is ${balance: .2f}")
def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("That's not a valid amount")
    elif


def withdraw():
    pass



balance = 0
is_running = True


while is_running:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("||                  BANKING SYSTEM                ||")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("1. Show Balance.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Exit..")

    choice = input("Enter your choice: ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")

print("Thank You, have a nice day")

