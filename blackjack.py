import random
print("welcome to the blackjack game")
pro_list = []
dealer_list = []
sum_lst = []
sum_tot=0
player_tot=0
l=1



card_list=['2♥️','3♥️','4♥️','5♥️','6♥️','7♥️','8♥️','9♥️','10♥️','K♥️','Q♥️','J♥️','A♥️',
	   '2💎️','3💎️','4💎️','5💎️','6💎️','7💎️','8💎️','9💎️','10💎️','K💎️','Q💎️','J💎️','A💎️',
	   '2♠️','3♠️','4♠️','5♠️','6♠️','7♠️','8♠️','9♠️','10♠️','K♠️','Q♠️','J♠️','A♠️',
	   '2♣️','3♣️','4♣️','5♣️','6♣️','7♣️','8♣️','9♣️','10♣️','K♣️','Q♣️','J♣️','A♣️']

number_card_list=['2♥️','3♥️','4♥️','5♥️','6♥️','7♥️','8♥️','9♥️','10♥️',
	   '2💎️','3💎️','4💎️','5💎️','6💎️','7💎️','8💎️','9💎️','10💎️',
	   '2♠️','3♠️','4♠️','5♠️','6♠️','7♠️','8♠️','9♠️','10♠️',
	   '2♣️','3♣️','4♣️','5♣️','6♣️','7♣️','8♣️','9♣️','10♣️']
	   
face_card_list=['K♥️','Q♥️','J♥️',
	   'K💎️','Q💎️','J💎️',
	   'K♠️','Q♠️','J♠️',
	   'K♣️','Q♣️','J♣️']	
	   
a_card_list=['A♥️','A💎️','A♠️','A♣️']

num=int(input("please enter the number of players "))

for i in range(1,num+1):
	a=random.choice(card_list)
	b=random.choice(card_list)
	print(f"The player{i} cards are")
	pro_list.append(a)
	pro_list.append(b)
	print(f"{a}  {b}")
	temp=0
	temp = a[0]
	if temp == 'K' or temp == 'Q' or temp == 'J':
		temp=10
	elif temp== 'A':
		temp=11
	
	temp1 = 0
	temp1 = b[0]	
	if temp1 == 'K' or temp1 == 'Q' or temp1== 'J':
		temp1=10
	elif temp1== 'A':
		temp1=11
	#print(a[0])
	#print(b[0])
	player_tot = int(temp) + int(temp1)
	sum_lst.append(player_tot)
	print(f"The player{i} points are: {str(player_tot)}")	
	#print(sum_lst)
	
	

for i in range(1,2):
	c=random.choice(card_list)
	d=random.choice(card_list)
	print(f"The dealer cards are")
	dealer_list.append(c)
	dealer_list.append(d)
	print(f"{c}  {d}")
	
for x in dealer_list:
	y=0
	y=x[0][0]
	if y== 'K' or y== 'Q' or y== 'J':
		y=10
	elif y== 'A':
		y=11
	sum_tot = sum_tot+int(y)		
	
print(f"dealer points is: {sum_tot}")	

for h in sum_lst:
	print(f"Dealer hand : {sum_tot}")
	print(f"Player{l} hand: {h}")
	if sum_tot > 21:
		print("Dealer busts")
	elif h > sum_tot:
		print(f"Player{l} win")
	elif h < sum_tot:
		print("Dealer win")
	else:
		print("its a tie")
	l=l+1
		
	
	






	   	      
	   	


