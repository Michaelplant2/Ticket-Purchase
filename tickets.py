import sys

TICKET_PRICE = 10
tickets_remaining = 100
service_charge = 2

def calculate_price(number_of_tickets):
    return number_of_tickets * TICKET_PRICE + service_charge

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?: ")
    num_tickets = input("How many tickets would you like, {}?: ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("Total due is ${}".format(amount_due))
        will_proceed = input("Do you want to proceed with the purchase?: Y/N  ")
        if will_proceed.upper() == "Y":
            print("Sold!")
            tickets_remaining -= num_tickets
        else: 
            print("Thank you anyway, {}".format(name))
print("Sorry sold out")

sys.exit()