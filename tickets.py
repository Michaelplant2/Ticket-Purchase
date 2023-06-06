import sys

TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining:

    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?: ")
    num_tickets = input("How many tickets would you like, {}?: ".format(name))
    num_tickets = int(num_tickets)
    amount_due = num_tickets * TICKET_PRICE
    print("Total due is ${}".format(amount_due))
    will_proceed = input("Do you want to proceed with the purchase?: Y/N  ")

    if will_proceed.upper() == "Y":
        print("Sold!")
        tickets_remaining -= num_tickets
    else: 
        print("Thank you anyway, {}".format(name))

print("Sorry sold out")

sys.exit()