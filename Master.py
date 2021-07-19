import random

def clear_page():
    print('\n' *35)

class Number_Card:
    all_numbers = {'Ace':[1,13], 'Two':[2,1], 'Three':[3, 2], 'Four':[4, 3], 'Five':[5, 4], 'Six':[6, 5], 'Seven': [7, 6], 'Eight':[8, 7], 'Nine': [9,8], 'Ten':[10, 9], 'Jack':[11, 10], 'Queen':[12, 11], 'King':[13, 12]}
    def __init__(self, point):
        self.card_name = list(Number_Card.all_numbers.keys())[point - 1]
        self.point = point
        self.rank = Number_Card.all_numbers[self.card_name][1]
    def __repr__(self):
        return self.card_name

class Card:
    numbers = [Number_Card(a) for a in range(1, 14)]
    suits = {'Diamonds':0, 'Clubs':0, 'Hearts':0, 'Spades':0}
    available_trump_suits = {'D': ['Diamonds', 20], 'C': ['Clubs', 20], 'H': ['Hearts', 30], 'S': ['Spades', 30],
                             'N': ['No Trump', 40]}
    final_contract = ''
    contract_made_player = []
    def __init__(self, number, suit):
        self.number = Card.numbers[number - 1]
        if Card.suits.get(suit, 100) != 100:
            self.suit = suit
        else:
            raise ValueError
    def __repr__(self):
        return "{Number} {Suit}".format(Number = self.number, Suit = self.suit)
    def __lt__(self, other):
        if Card.suits[self.suit] == Card.suits[other.suit] and self.number.rank < other.number.rank:
            return True
        elif Card.suits[self.suit] < Card.suits[other.suit]:
            return True
        else:
            return False
    def __gt__(self, other):
        if Card.suits[self.suit] == Card.suits[other.suit] and self.number.rank > other.number.rank:
            return True
        elif Card.suits[self.suit] > Card.suits[other.suit]:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.number == other.number and Card.suits[self.suit] == Card.suits[other.suit]:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.number != other.number and Card.suits[self.suit] != Card.suits[other.suit]:
            return True
        else:
            return False
    def set_trump(trump):
        Card.suits[trump] = 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
all_cards = [Card(number, suit) for number in numbers for suit in suits]

class Player:
    def __init__(self, name, team_num):
        self.name = name
        self.holding_cards = []
        self.team = team_num
        count = 0
        upper_limit = len(all_cards)
        self.win_count = 0
        while count < 13:
            count += 1
            upper_limit -= 1
            random_number = random.randint(0,upper_limit)
            self.holding_cards.append(all_cards[random_number])
            all_cards.pop(random_number)
        def sort_suit(card):
            return card.suit
        self.holding_cards.sort()
        self.holding_cards.sort(key=sort_suit)

    def __repr__(self):
        return self.name
    def __eq__(self, other):
        if self.name == other.name:
            return True
    def __ne__(self, other):
        if self.name != other.name:
            return True
    def add_win(self):
        self.win_count += 1

class Team():
    def __init__(self, player_1, player_2):
        self.player1 = player_1
        self.player2 = player_2
    def __repr__(self):
        return ('{player1}, {player2}'.format(player1 = self.player1, player2 = self.player2))

print('Welcome to Bridge, this is a four people strategic game. You will take hold of the computer when it is your turn and pass along when your turn is over. Let\'s start!')

player1 = Player(input('''
What is the name of the first player?
'''), 1)
print('''
These are your cards
''')
print(player1.holding_cards)
input('To pass turn, enter anything.')
clear_page()

player2 = Player(input('''
What is the name of the second player?
'''), 2)
print('''
These are your cards
''')
print(player2.holding_cards)
input('To pass turn, enter anything.')
clear_page()

player3 = Player(input('''
What is the name of the third player?
'''), 1)
print('''
These are your cards
''')
print(player3.holding_cards)
input('To pass turn, enter anything.')
clear_page()

player4 = Player(input('''
What is the name of the last player?
'''), 2)
print('''
These are your cards
''')
print(player4.holding_cards)
input('To initiate calling sequence, enter anything.')
clear_page()

team1 = Team(player1, player3)
team2 = Team(player2, player4)

class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.cards_played = []
    def __repr__(self):
        return 'Round {}'.format(str(round_number))
    def play_round(self, previous_winning_player = player1):
        all_players = [player1, player2, player3, player4]
        play_order = []
        starting_player_index = all_players.index(previous_winning_player)
        play_order.append(previous_winning_player)
        adding_player_index = 0
        adding_player_index += starting_player_index + 1
        starting_suit = ''
        player_card_suit = ''
        player_card_value = 0
        for i in range(3):
            if adding_player_index == len(all_players):
                adding_player_index = 0
                play_order.append(all_players[adding_player_index])
                adding_player_index += 1
            else:
                play_order.append(all_players[adding_player_index])
                adding_player_index += 1
        for player in play_order:
            a = 0
            player_card_suit = ''

            #each player playing their card
            def ask_for_card():
                nonlocal player_card_suit
                nonlocal starting_suit
                nonlocal play_order
                nonlocal player_card_value
                nonlocal a

                if self.cards_played != []:
                    print('The cards having been played in order are {cards}.'.format(cards=self.cards_played))
                    print('\n')
                if player.name != opening_cards_player.name:
                    print('{player_name}\'s cards are opened below.'.format(player_name=opening_cards_player.name))
                    print(opening_cards_player.holding_cards)
                    print('\n')

                print('It is your turn, {player_name}. These are your cards. Please indicate which card you would like to play.'.format(player_name=player.name))
                print(player.holding_cards)
                print('\n')
                # ace number = 1, jack number = 11, queen number = 12, king number = 13
                player_input = input('What value?')
                if player_input.upper() == 'ACE':
                    player_card_value = 1
                elif player_input.upper() == 'JACK':
                    player_card_value = 11
                elif player_input.upper() == 'QUEEN':
                    player_card_value = 12
                elif player_input.upper() == 'KING':
                    player_card_value = 13
                else:
                    player_card_value = int(player_input)

                player_card_suit_input = input('What suit?')
                if player_card_suit_input.upper() == 'SPADES':
                    player_card_suit = 'Spades'
                elif player_card_suit_input.upper() == 'HEARTS':
                    player_card_suit = 'Hearts'
                elif player_card_suit_input.upper() == 'CLUBS':
                    player_card_suit = 'Clubs'
                elif player_card_suit_input.upper() == 'DIAMONDS':
                    player_card_suit = 'Diamonds'
                test_card = Card(player_card_value, player_card_suit)
                if not test_card in player.holding_cards:
                    raise ValueError
                a += 1

            while a == 0:
                try:
                    ask_for_card()
                except NameError:
                    print('This is an invalid entry, please try again.')
                except ValueError:
                    print('This is an invalid entry, please try again.')
                except KeyError:
                    print('This is an invalid entry, please try again.')
                except IndexError:
                    print('This is an invalid entry, please try again.')
            if play_order.index(player) == 0:
                first_player_suit = player_card_suit
                Card.suits[first_player_suit] += 1
                starting_suit += first_player_suit
                player_card = Card(player_card_value, player_card_suit)

            if player_card_suit != starting_suit and starting_suit in [card.suit for card in player.holding_cards]:
                print("The current legal suit is {suit}".format(suit=starting_suit))
                while player_card_suit != starting_suit and starting_suit in [card.suit for card in
                                                                              player.holding_cards]:
                    print('This is an invalid card, please try again.')
                    ask_for_card()

            player_card = Card(player_card_value, player_card_suit)
            self.cards_played.append(player_card)
            player.holding_cards.remove(player_card)
            print('Your remaining cards are {}'.format(player.holding_cards))
            input('To pass turn, enter anything.')
            clear_page()
        self.winning_card = max(self.cards_played)
        Card.suits[first_player_suit] -= 1
        winning_player = None
        if self.cards_played.index(self.winning_card) == play_order.index(player1):
            winning_player = player1
            player1.add_win()
        elif self.cards_played.index(self.winning_card) == play_order.index(player2):
            winning_player = player2
            player2.add_win()
        elif self.cards_played.index(self.winning_card) == play_order.index(player3):
            winning_player = player3
            player3.add_win()
        elif self.cards_played.index(self.winning_card) == play_order.index(player4):
            winning_player = player4
            player4.add_win()
        print('The winning player of this round is {player_name} with the {card_name}.'.format(
            player_name=winning_player.name, card_name=self.winning_card))

        print('''
            {Team1} currently have {Team1_stacks} stack(s) won, and {Team2} have {Team2_stacks} stack(s) won. 
            '''.format(Team1=team1, Team1_stacks=player1.win_count + player3.win_count, Team2=team2,
                       Team2_stacks=player2.win_count + player4.win_count))

        if (player1 or player3 in Card.contract_made_player) and int(Card.final_contract[0]) + 6 - (
                player1.win_count + player3.win_count) >= 1:
            print('''
             {stacks_remaining_to_fulfill_contract} more stacks need to be won for the contract to be fulfilled.
             '''.format(stacks_remaining_to_fulfill_contract=int(Card.final_contract[0]) + 6 - (
                        player1.win_count + player3.win_count)))
        elif (player2 or player4 in Card.contract_made_player) and int(Card.final_contract[0]) + 6 - (
                player2.win_count + player4.win_count) >= 1:
            print('''
             {stacks_remaining_to_fulfill_contract} more stacks need to be won for the contract to be fulfilled.
             '''.format(stacks_remaining_to_fulfill_contract=int(Card.final_contract[0]) + 6 - (
                        player2.win_count + player4.win_count)))
        else:
            print('''
                The contract is already fulfilled.
                ''')
        input('To continue, enter anything.')
        clear_page()
        return winning_player

round1 = Round(1)
round2 = Round(2)
round3 = Round(3)
round4 = Round(4)
round5 = Round(5)
round6 = Round(6)
round7 = Round(7)

def calling_sequence():
    final_amount = 0
    final_how_many = 0
    pass_count = 0
    ultimate_count = 0
    invalid_count = 0
    call_count = 0
    current_call = ''
    player_calling_order_updated_by_winning_call = [player1, player2, player3, player4]

    available_trump_suits = {'D': ['Diamonds', 20], 'C': ['Clubs', 20], 'H': ['Hearts', 30], 'S': ['Spades', 30],
                             'N': ['No Trump', 40]}
    # already in universal scope: suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    print('Now, we will begin the calling sequence.')
    def individual_call():
        nonlocal pass_count
        nonlocal final_amount
        nonlocal final_how_many
        nonlocal current_call
        nonlocal invalid_count
        nonlocal ultimate_count
        nonlocal call_count
        nonlocal player_calling_order_updated_by_winning_call

        #function so that when the index of the call winning player is passed, it returns a list with the winning player as first and the players who will later call in order.
        # e.g. if player3 won, the function will pass 2 and return [player3, player4, player1, player2] and then the call_count will reset. Then later, when the final winning call is determined, this function can be used to
        # trace the winning player by providing the list and the programmer needs only to get the result of this function and obtain its first element. This funciton will only be called
        # if there is a successful bid.

        def get_player(call_winning_player_index = 0):
            nonlocal player_calling_order_updated_by_winning_call
            all_players = player_calling_order_updated_by_winning_call
            play_order = []
            call_winning_player = all_players[call_winning_player_index]
            play_order.append(call_winning_player)
            adding_player_index = 0
            adding_player_index += call_winning_player_index + 1
            for i in range(3):
                if adding_player_index == len(all_players):
                    adding_player_index = 0
                    play_order.append(all_players[adding_player_index])
                    adding_player_index += 1
                else:
                    play_order.append(all_players[adding_player_index])
                    adding_player_index += 1
            player_calling_order_updated_by_winning_call = play_order

        if current_call == '':
            print('''
            There is no currently contract
            ''')
        else:
            print(''' 
            The current contract is {amount} {suit} called by {name}.
            '''.format(amount=current_call[0], suit=available_trump_suits.get(current_call[1])[0], name=player_calling_order_updated_by_winning_call[0].name))
        print('These are your cards, {name}'.format(name=player_calling_order_updated_by_winning_call[player_calling_order_updated_by_winning_call.index(player_calling_order_updated_by_winning_call[call_count])].name))
        print(player_calling_order_updated_by_winning_call[player_calling_order_updated_by_winning_call.index(player_calling_order_updated_by_winning_call[call_count])].holding_cards)
        player_call = input('''
        What would you like to call? e.g. Enter 1S for One Spade, 1N for 1 No Trump etc. If pass, enter pass. Please CALL OUT your decision.
        ''')
        if invalid_count == 2 and pass_count == 2 and current_call == '':
            pass_count -= 1
        try:
            if player_call.lower() != 'pass' and player_call != '' \
                                                                '':
                player_call_trump = available_trump_suits.get(player_call[1])[0]
                how_many = int(player_call[0])
                point_total = int(player_call[0]) * available_trump_suits.get(player_call[1])[1]
                if point_total > final_amount and how_many <= 7:
                    get_player(player_calling_order_updated_by_winning_call.index(
                        player_calling_order_updated_by_winning_call[call_count]))
                    final_amount = point_total
                    pass_count = 0
                    invalid_count = 0
                    call_count = 0
                    call_count += 1
                    current_call = player_call
                    print('This is a valid contract.')
                    print('\n')
                    input('To pass turn, enter anything.')
                    clear_page()
                    return player_call
                elif point_total <= final_amount or how_many > 7:
                    print('This is an invalid contract, your turn is passed.')
                    pass_count += 1
                    invalid_count += 1
                    call_count += 1
                    if current_call == '':
                        print('''
                        There is no contract
                        ''')
                        input('To pass turn, enter anything.')
                        clear_page()
                        return current_call
                    else:
                        print('''
                        The current contract is {amount} {suit}
                        '''.format(amount=current_call[0], suit=available_trump_suits.get(current_call[1])[0]))
                        input('To pass turn, enter anything.')
                        clear_page()
                        return current_call
            elif player_call.upper() == 'PASS' or player_call == '' \
                                                                 '':
                pass_count += 1
                call_count += 1
                if current_call == '':
                    print('''
                    There is no contract
                    ''')
                    input('To pass turn, enter anything.')
                    clear_page()
                    while pass_count == 2 and ultimate_count < 1:
                        pass_count -= 1
                        ultimate_count += 1
                    return current_call
                input('To pass turn, enter anything.')
                clear_page()
                return current_call
        except IndexError:
            player_call = input('''
        What would you like to call? e.g. Enter 1S for One Spade, 1N for 1 No Trump etc. If pass, enter pass.
        ''')
            print('Please try again, as they were both invalid entries.')
        except TypeError:
            player_call = input('''
        What would you like to call? e.g. Enter 1S for One Spade, 1N for 1 No Trump etc. If pass, enter pass.
        ''')
            print('Please try again, as they were both invalid entries. You had two chances, do better.')





    while pass_count < 3:
        final_contract = individual_call()

    if final_contract != '':
        final_amount += int(final_contract[0]) * available_trump_suits.get(final_contract[1])[1]
        final_how_many += int(final_contract[0])
        print('''
        The final contract is {amount} {suit}.
        '''.format(amount=final_how_many, suit=available_trump_suits.get(final_contract[1])[0]))
        Card.set_trump(available_trump_suits.get(final_contract[1])[0])
        Card.final_contract += str((final_how_many))
        Card.final_contract += (final_contract[1])
        Card.contract_made_player.append(player_calling_order_updated_by_winning_call[0])
        return player_calling_order_updated_by_winning_call[0]

    else:
        print('''
        No contract is made, game restarts.''')
        quit()


#calling sequence and time to play rounds
contract_making_player = calling_sequence()
if contract_making_player == player1:
    opening_cards_player = player3
elif contract_making_player == player3:
    opening_cards_player = player1
elif contract_making_player == player2:
    opening_cards_player = player4
elif contract_making_player == player4:
    opening_cards_player = player2



round7.play_round((round6.play_round(round5.play_round(round4.play_round(round3.play_round(round2.play_round(round1.play_round(contract_making_player))))))))

#showing game result
if (player1 or player3 in Card.contract_made_player):
    if int(Card.final_contract[0]) + 6 <= player1.win_count + player3.win_count:
        print('''
        {Contract is fulfilled. {Team1} gain {points} points!}
        '''.format(
        Team1=team1, points= int(Card.final_contract[0])*Card.available_trump_suits[[Card.final_contract[1]]][1]))
    else:
        print('''
        Contract is not fulfilled. {Team1} lose {points} points.
        '''.format(Team1=team1, points= int(Card.final_contract[0])*Card.available_trump_suits[[Card.final_contract[1]]][1]))
if (player2 or player4 in Card.contract_made_player):
    if int(Card.final_contract[0]) + 6 <= player2.win_count + player4.win_count:
        print('''
        {Contract is fulfilled. {Team2} gain {points} points!}
        '''.format(
        Team2=team2,
        points=int(Card.final_contract[0]) * Card.available_trump_suits[[Card.final_contract[1]]][1]))
    else:
        print('''
        Contract is not fulfilled. {Team2} lose {points} points.
        '''.format(Team2=team2, points=int(Card.final_contract[0]) * Card.available_trump_suits[[Card.final_contract[1]]][1]))

