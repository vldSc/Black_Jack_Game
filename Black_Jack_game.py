import random
from art import win_bj as win, bj
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
decisions = ["h","s"]
answer_yn = ["y","n"]
max_points = 21

def validation(response, answer):
    '''Check if user's response is valid '''
    if response in answer:
        return True
    else:
        print("\nUpps, it looks like you choose an invalid option. Please choose a valid one!")
        return False

def point_str(points):
    points_str = ', '.join(map(str, points))
    return points_str

def verification_ace(points):
    index = points.index(11)
    points[index] = 1

    return points

def display_points(points, total, person):
    points_str = point_str(points)

    if total <= max_points:
        print(f"\n{person} cards are: {points_str} total points: {total}")
    else:
        print(f"\n{person} cards are: {points_str} total points: too many")

def calc_player_points(points):
    person = "Player's"
    total_player = sum(points)

    if total_player > max_points and 11 in points:
        points = verification_ace(points)
        total_player = sum(points)
        display_points(points,total_player, person)
    else:
        display_points(points,total_player, person)

    if total_player < max_points:
        check = False
        while not check:
            answer = input("What would you like to do next?  Type 'h' for hit or 's' for stand: ")
            check = validation(answer, decisions)

        if answer == "h":
            points.append(random.choice(cards))
            return calc_player_points(points)
        else:
            return total_player
    else: 
        return total_player

        
def calc_dealer_points(points):
    person = "Dealer's"
    total_dealer = sum(points)
    
    if total_dealer > max_points and 11 in points:
        points = verification_ace(points)
        total_dealer = sum(points)
        display_points(points,total_dealer, person)
    else: 
        display_points(points, total_dealer, person)
    
    if total_dealer <= 16:
        points.append(random.choice(cards))
        return calc_dealer_points(points)
    else: 
        return total_dealer

def get_winner(dealer, player):
    dealer_result = "too many" if dealer > max_points else dealer
    player_result = "too many" if player > max_points else player

    if dealer == player:
        result = "It's a draw!"
    elif dealer_result == "too many" or (player_result != "too many" and dealer < player):
        result = "Player wins!\nCongratulations!"
        print(win)
    else:
        result = "Dealer wins!"

    print(f"\nDealer has {dealer_result} and player has {player_result}. {result}")

def display_cards(player_points, dealer_points):
    print(f"\nPlayer's cars are: {player_points[0]}, {player_points[1]}")
    print(f"Dealer's cards are: {dealer_points[0]}, {dealer_points[1]}")

def black_jack(score, person):
    if person == "Player":
        print(win)
        print(f"\nBlackjack! Player wins with a beautiful Blackjack! Dealer has {score} points.")
    else:
        print(f"\n{person} has a Black Jack! Player has {score}. Best luck on a next game!")


def bj_game():
    clear()
    print(bj)
    player_points = []
    dealer_points = []

    for i in range (2):
        player_points.append(random.choice(cards))
        dealer_points.append(random.choice(cards))

    if sum(player_points) == sum(dealer_points):
        display_cards(player_points, dealer_points)
        get_winner(sum(player_points), sum(dealer_points))
    elif sum(player_points)== 21:
        display_cards(player_points, dealer_points)
        black_jack(score= sum(dealer_points), person = "Player")
    elif sum(dealer_points) == 21:
        display_cards(player_points, dealer_points)
        black_jack( score= sum(player_points), person="Dealer")
    else:
        print(f"Dealer's open card is: {dealer_points[0]}")

        total_players_points = calc_player_points(player_points)

        if total_players_points >= max_points:
            total_dealer_points = sum(dealer_points)
            get_winner(total_dealer_points, total_players_points)
        else: 
            total_dealer_points = calc_dealer_points(dealer_points)
            get_winner(total_dealer_points, total_players_points)


    check = False
    while not check:
        answer = input("\nDo you want to play again? Please type 'y' for yes or 'n' for no: ")
        check = validation(answer, answer_yn)

    if answer == "y":
        bj_game()
    else:
        print("\nSee you next time!")

bj_game()

