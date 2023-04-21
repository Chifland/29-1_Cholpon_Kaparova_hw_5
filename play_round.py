from random import choices
# from decouple import config
# money = config('My_Money', cast=int)
def play_round():
    number_list = list(range(1, 31))
    bet = int(input(f'Enter your bet for 1st slot:'))
    # bet_2 = input(f'Enter your bet for 2nd slot:')
    money = int(input(f'Enter your money '))
    # bet = [bet_1, bet_2]
    win = choices(number_list, k=5)
    for num in win:
        if bet == num:
            money *= 2
            print(f'You win {money} , slot: {win}')
            break
    else:
        money -= money
        print(f'You lost your money {money}\nNumbers in slot: {win}')




