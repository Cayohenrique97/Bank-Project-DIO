menu = """

 [D] Deposit
 [W] Withdraw
 [E] Extract
 [Q] Quit

 --> """

balance = 0
limit = 500
extract = ""
witdraw_number = 0
withdraw_limit = 3


while True:

    # deposito
    option = input(menu).upper()

    if option == "D":
        value = float(input("Enter the amount deposit: "))

        if value > 0:
            balance += value
            extract += f"Deposit: R${value:.2f}\nNew balance: {balance}\n\n"
            print(f"Your amount: {balance}")
        else:
            print("Operation Failed! Negative amount")

    # Saque
    elif option == "W":

        value = float(input("Enter the amount withdraw: "))

        if balance > 0 and value < balance:
            if value > 0 and value <= 500 and withdraw_limit <= 3:
                balance -= value
                extract += f"Withdraw: R${value:.2f}\nNew balance: {balance}\n\n"
                print(f"Your amount: {balance}")
                witdraw_number += 1

            else:
                print("Operation failed!")
        else:
            print("Operation failed!")

    # Extrato
    elif option == "E":
        print("==========================")

        print("Extract")
        print("--------------------------")
        print(extract)

        print("==========================")
    elif option == "Q":
        break

    else:
        print("Invalid key,try another")
