from replit import clear
print("Welcome to the secret auction program!")

def highest_bidder(bid_record):
  highest = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest:
      highest = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest}")

mapp = {}

restart = True
while restart:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  mapp[name] = bid
  other_bidders = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
  if other_bidders == "yes":
    restart = True
    clear()
  else:
    restart = False
    highest_bidder(mapp)



