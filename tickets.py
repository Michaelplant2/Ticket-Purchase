TICKET_PRICE = 10

tickets_remaining = 100

print("There are {} tickets remaining.".format(tickets_remaining))

name = input("What is your name: ")

num_tickets = input("How many tickets would you like, {}: ".format(name))
num_tickets = int(num_tickets)

amount_due = num_tickets * TICKET_PRICE

print("Total due is ${}".format(amount_due))