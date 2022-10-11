import random as rd

amount = rd.randint(4, 30)
print(amount)
pc = 0
while amount > 1:
    user = int(input("Your turn (print 1 or 2 or 3)"))
    amount = amount - user
    if amount == 1:
        print("Congratulations! You won this game!")
        break
    else:
        print(amount, " stones in the box after your turn")
    if amount > 3:
        pc = rd.randint(1, 3)
    if amount == 3:
        pc = rd.randint(1, 2)
    if amount == 2:
        pc = rd.randint(1, 1)
    amount = amount - pc
    if amount == 1:
        print("Sorry, you lose. Try again!")
    else:
        print(amount, " stones in the box after pc's turn")
