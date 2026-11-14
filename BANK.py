import sys

def details(name,initial_balance,deposit,withdraw,total_balance):
    print("Customer Name: ", name)
    print("Initial Balance: ", initial_balance)
    print("Balance after deposit ", deposit)
    print("Balance after withdrawal: ", withdraw)

name = sys.argv[1]
inital_balance = int(sys.argv[2])
deposit = int(sys.argv[3])
total_balance = inital_balance + deposit


withdraw = input(sys.argv[4])
total_balance = total_balance - withdraw

print("Total balance is ",total_balance)

if __name__ == "__main__":
  if total_balance < 1000:
     print("minimum balance must be 1000")