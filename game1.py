print('Nhap Dam, La hoac Keo')
player=input()
from random import randint
computer= randint(0,2)
if computer == 0:
	computer= 'Dam'
if computer ==1:
	computer = 'La'
if computer ==2:
	computer= "Keo"
print('Ban da chon '+ player)
print('May tinh chon '+ computer)

if player==computer:
	print("Hoa")
elif player == "Dam":
	if computer == "La":
		print("Ban da thua") 
	if computer=='Keo':
		print ("Ban da thang")
elif player=="La":
	if computer == "Keo":
		print ("Ban da thua")
	if computer=="Dam":
		print("Ban da thang") 
elif player=="Keo":
	if computer=="Dam":
		print('Ban da thua')
	if computer=="La":
		print("Ban da thang")
else:
	print("Nhap sai")
	