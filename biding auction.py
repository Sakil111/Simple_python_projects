bid={}
biding_finish=False

def higgest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
    print(f"The winning bid price is {bid_amount} and bidder is {bidder}")

while not biding_finish:
    name=input("Enter your name: ")
    price=int(input("Enter your bid: "))
    bid[name]=price
    should_continue=input("Are there any other bidder types 'yes' or 'no' ")
    if should_continue=="no":
        biding_finish=True
        higgest_bidder(bid)



