name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
db_persons = {
    name: bid,
}

while True:
    any_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_other_bidder == "yes":
        print("\n" * 20)
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        db_persons[name] = bid
    else:
        break

highest_bidder = ""
highest_bid = 0

for key in db_persons:
    if db_persons[key] > highest_bid:
        highest_bid = db_persons[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
