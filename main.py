from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

# Put logo
print(art.logo)
all_bid = {} 


more_bid = True
while more_bid: 
  # ask name
  bidder_name = input("What is your name? ")
  # ask bid
  bidder_bid = int(input("What is your bid? $"))
  

  all_bid[bidder_name] = bidder_bid
  any_more_bid = input("Are there any other bidder? Type 'yes' or 'no' ").lower()
  
  if any_more_bid == 'yes':      
    clear()
  else:
    more_bid = False
    
the_winner = 0
the_max_bid = 0

for i in all_bid:
  if all_bid[i] > the_max_bid:
    the_max_bid = all_bid[i] 
    the_winner = i
    
# # function to return key for any value
# def get_key(val):
#     for key, value in all_bid.items():
#          if val == value:
#              return key
 
print(f"{the_winner} get the highest bid  {the_max_bid}")
  



 