from datetime import datetime, timedelta
import textwrap


def menu():
    menu = """ \n

    <===============Select the Option ======================>

    [D]\tDeposit
    [W]\tWithdraw
    [E]\tExtract
    [NA]\tNew Account
    [LC]\tList Account
    [NU]\tNew User
    [Q]\tQuit

    ===> """
    return input(textwrap.dedent(menu))


# ACEITA APENAS DADOS SEM NOMEAÇÃO
def deposit(balance, value, extract, /):
    date_now = datetime.today()
    if value > 0:
        balance += value
        extract += f"Deposit: R${value:.2f}\nNew balance: {balance}\n{date_now.strftime('%d/%m/%Y - %H:%M')}\n"
        print(f" -----> Deposit success. <------ \n")
        print(f" -----> Your amount: {balance} <------ ")
    else:
        print(" ~~~~~~~:> Operation Failed! Negative amount  <:~~~~~~~ ")

    return balance, extract

# DEPOIS DO * TUDO TEM QUE SER NOMEADO


def withdraw(*, balance, value, extract, limit, withdraw_number, withdraw_limit):
    date_now = datetime.today()
    exceeded_value = value > balance
    exceeded_limit = value > limit
    exceeded_withdraw = withdraw_number >= withdraw_limit

    if exceeded_value:
        print(" ~~~~~~~:> Operation Failed! You don't have balance  <:~~~~~~~")

    elif exceeded_limit:
        print(
            f" ~~~~~~~:> Operation Failed! You don't have limit, your limit is: {limit} <:~~~~~~~")

    elif exceeded_withdraw:
        print(" ~~~~~~~:> Operation Failed! You exceeded your withdraw limit.  <:~~~~~~~")

    elif value > 0:
        balance -= value
        print(f" -----> Withdraw success. <------ \n")
        extract += f"Withdraw: R${value:.2f}\nNew balance: {balance}\n{date_now.strftime('%d/%m/%Y - %H:%M')}\n"
        print(f"Your amount: {balance}")
        withdraw_number += 1
    else:
        print(" ~~~~~~~:> Operation Failed! Negative value  <:~~~~~~~")

    return balance, extract, withdraw_number


def show_extract(extract):
    date_now = datetime.today()
    print("==========================")

    print("Extract")
    print("--------------------------")
    print(extract)

    print("==========================")
    print(date_now.strftime('%d/%m/%Y - %H:%M'))


def create_user(users):
    cpf = input("Insert your CPF (just numbers): ")
    user = filter_user(cpf, users)

    if user:
        print("\n Already exist a user with this CPF")
        return
    name = input("Inser your full name: ")
    born_date = input("Insert your born date (dd-mm-aaaa): ")
    address = input("Inser your address: ")

    users.append({"name": name, "born_date": born_date,
                 "cpf": cpf, "address": address})
    print("Succssesfull!!! User created")


def filter_user(cpf, users):
    filtred_user = [user for user in users if user["cpf"] == cpf]
    return filtred_user[0] if filtred_user else None


def create_account(Bank_agency, accounts_number, users):
    cpf = input("Inser your CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("\n Account created successfully!")
        return {"Bank_agency": Bank_agency, "accounts_number": accounts_number, "users": user}

    print("User not found, you must create a user first")


def list_account(accounts):
    for account in accounts:
        line = f"""\
        Agency:\t{account['Bank_agency']}
        C/C:\t\t{account['accounts_number']}
        Holder:\t{account['users']['name']}
    """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    Bank_Agency = "0001"
    balance = 0
    limit = 500
    extract = ""
    withdraw_number = 0
    withdraw_limit = 3
    users = []
    accounts = []
    while True:

        # deposit
        option = menu().upper()

        if option == "D":

            value = float(input("Enter the amount deposit: "))
            balance, extract = deposit(balance, value, extract)
        # Saque
        elif option == "W":
            value = float(input("Enter the amount withdraw: "))
            balance, extract, withdraw_number = withdraw(balance=balance,
                                                         value=value,
                                                         extract=extract,
                                                         limit=limit,
                                                         withdraw_number=withdraw_number,
                                                         withdraw_limit=withdraw_limit,)
        # Extrato
        elif option == "E":
            show_extract(extract)

        elif option == "NU":
            create_user(users)

        elif option == "NA":
            accounts_number = len(accounts) + 1
            account = create_account(Bank_Agency, accounts_number, users)

            if account:
                accounts.append(account)

        elif option == "LC":
            list_account(accounts)

        elif option == "Q":
            break

        else:
            print("Invalid key,try another")


main()
