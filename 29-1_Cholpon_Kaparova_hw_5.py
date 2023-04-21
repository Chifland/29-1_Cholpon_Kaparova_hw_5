from play_round import play_round
from decouple import config
def game_play():
    play_round()
    while True:
        choice = input(f'Do you want to continue playing? Please enter y or n')
        if choice == 'n':
            print(f'Good luck')
            break
        elif choice == 'y':
            play_round()
game_play()
deactiva


