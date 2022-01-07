# number guessing game
num = 44
guess = int(input('enter your number which you want:'))
if guess > 0:
    if num == guess:
        print('you win')
    else:
        if num < guess:
            print('your number is higher then actual number')
        if num > guess:
            print('your number is smaller then actual number')
else:
    print('0 is not valid number')
##############################################################

