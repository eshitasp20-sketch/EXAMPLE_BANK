import sys

def details(name,initial_balance,deposit,withdraw):
    print("Customer Name: ", name)
    print("Initial Balance: ", initial_balance)
    print("Balance after deposit ", deposit)
    print("Balance after withdrawal: ", withdraw)


if __name__ == "__main__":
    name = sys.argv[1]
    initial_balance = int(sys.argv[2])
    deposit = int(sys.argv[3])
    total_balance = initial_balance + deposit
    withdraw = int(sys.argv[4])
    total_balance = total_balance - withdraw

    print("Total balance is ",total_balance)

    print("\nCustomer Details")
    print("--------------")
    print(details(name, initial_balance, deposit, withdraw))

if total_balance < 1000:
    print("minimum balance must be 1000")